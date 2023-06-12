from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math
from django.template.loader import render_to_string
from userapp.models import *
from datetime import datetime
from .investment_analysis_methods import *
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.


def analysis(request):
    return HttpResponse("<h1>Welcome to Analysis</h1>")


#############Residential###############


def residential(request):
    data = {}
    if request.GET.get("id"):
        report_id = int(request.GET.get("id"))
        reportsdata = Reports.objects.filter(id=report_id).first()
        data["reportsdata"] = reportsdata
        tenants = Tenants.objects.filter(report_id=report_id)
        data["tenants"] = tenants
        data["tenants_count"] = tenants.count()
        additional_incomes = Subheads.objects.filter(report_id=report_id, type="income")
        data["additional_income"] = additional_incomes
        data["additional_income_count"] = additional_incomes.count()
        additional_expenses = Subheads.objects.filter(
            report_id=report_id, type="expense"
        )
        data["additional_expenses"] = additional_expenses
        data["additional_expenses_count"] = additional_expenses.count()
        data["clo_exp"] = Subheads.objects.filter(
            report_id=report_id, type="closing_expense"
        )
        data["sum_clo_conc"] = Subheads.objects.filter(
            report_id=report_id, type="closing_consession"
        ).aggregate(Sum("amount"))["amount__sum"]
        data["sum_clo_exp"] = Subheads.objects.filter(
            report_id=report_id, type="closing_expense"
        ).aggregate(Sum("amount"))["amount__sum"]
        data["clo_con"] = Subheads.objects.filter(
            report_id=report_id, type="closing_consession"
        )
        data["expenses"] = Subheads.objects.filter(report_id=report_id, type="expense")
        # print(data)
    else:
        data["reportsdata"] = ""
    # data["reportsdata"] = {"cloned": 0}
    return render(request, "residential.html", data)


def residential_analysis(request):
    form_data = request.POST.get("form_data")
    edited_post_data = QueryDict(form_data.replace("_edit", ""))
    request.POST = edited_post_data
    # print(request.POST)
    residential_data = {}
    residential_data["dynamic_input_update"] = {}
    if request.POST:
        tenant_name = request.POST.get("tenant_name")
        property_mgmt_type = int(request.POST.get("property_mgmt_type"))
        expense_vacancy_type = int(request.POST.get("expense_vacancy_type"))
        expense_maintenance_type = int(request.POST.get("expense_maintenance_type"))
        balance = 0
        if request.POST.get("original_purchase_price"):
            balance = float(request.POST.get("original_purchase_price"))
        closing_concession = request.POST.get("closing_consessions_view")
        if not closing_concession.strip():
            closing_concession = 0
        closing_expenses = request.POST.get("closing_expenses_view")
        if not closing_expenses.strip():
            closing_expenses = 0

        sft_leased = request.POST.get("sft_leased")

        if not sft_leased:
            sft_leased = 0
        else:
            sft_leased = int(sft_leased)

        lease_rate = request.POST.get("lease_rate")

        if not lease_rate:
            lease_rate = 0
        else:
            lease_rate = int(lease_rate)

        gross_income = request.POST.get("gross_income")
        rent_increases = request.POST.get("rent_increases")
        rent_increase_value = request.POST.get("rent_increase_value")
        rent_increases_for_every_year = request.POST.get(
            "rent_increases_for_every_year"
        )
        amount_down_payment_type = int(request.POST.get("amount_down_payment_type"))
        if request.POST.get("amount_down_payment_value"):
            amount_down_payment_value = float(
                request.POST.get("amount_down_payment_value")
            )
        else:
            amount_down_payment_value = 0
        if not amount_down_payment_value:
            amount_down_payment_value = 0

        asset_appraisal_type = int(request.POST.get("asset_appraisal_type"))
        if request.POST.get("asset_appraisal_value"):
            asset_appraisal_value = float(request.POST.get("asset_appraisal_value"))
        else:
            asset_appraisal_value = 0
        sales_expense_type = int(request.POST.get("sales_expense_type"))
        if request.POST.get("sales_expense_value"):
            sales_expense_value = float(request.POST.get("sales_expense_value"))
        else:
            sales_expense_value = 0

        lease_rate_type = request.POST.get("lease_rate_type")

        if request.POST.get("expense_maintenance"):
            expense_maintenance = float(request.POST.get("expense_maintenance"))
        else:
            expense_maintenance = 0
        if request.POST.get("expense_vacancy"):
            expense_vacancy = float(request.POST.get("expense_vacancy"))
        else:
            expense_vacancy = 0
        if request.POST.get("property_mgmt"):
            property_mgmt = float(request.POST.get("property_mgmt"))
        else:
            property_mgmt = 0
        if request.POST.get("expense_taxes"):
            expense_taxes = int(request.POST.get("expense_taxes"))
        else:
            expense_taxes = 0
        taxes_ye_mo = int(request.POST.get("taxes_ye_mo"))
        taxes_frequency = int(request.POST.get("taxes_frequency"))
        taxes_increases_type = int(request.POST.get("taxes_increases_type"))
        if request.POST.get("taxes_increase_value"):
            taxes_increase_value = int(request.POST.get("taxes_increase_value"))
        else:
            taxes_increase_value = 0
        if request.POST.get("taxes_increases_for_every_year"):
            taxes_increases_for_every_year = int(
                request.POST.get("taxes_increases_for_every_year")
            )
        else:
            taxes_increases_for_every_year = 0

        if request.POST.get("expense_hoa"):
            expense_hoa = float(request.POST.get("expense_hoa"))
        else:
            expense_hoa = 0
        hoa_ye_mo = int(request.POST.get("hoa_ye_mo"))
        hoa_frequency = int(request.POST.get("hoa_frequency"))
        hoa_increases_type = int(request.POST.get("hoa_increases_type"))
        if request.POST.get("hoa_increase_value"):
            hoa_increase_value = float(request.POST.get("hoa_increase_value"))
        else:
            hoa_increase_value = 0
        hoa_increases_for_every_year = int(
            request.POST.get("hoa_increases_for_every_year")
        )
        if request.POST.get("insurance_expense"):
            insurance_expense = float(request.POST.get("insurance_expense"))
        else:
            insurance_expense = 0
        insu_ye_mo = int(request.POST.get("insu_ye_mo"))
        insu_frequency = int(request.POST.get("insu_frequency"))
        insu_increases_type = int(request.POST.get("insu_increases_type"))
        if request.POST.get("insu_increase_value"):
            insu_increase_value = float(request.POST.get("insu_increase_value"))
        else:
            insu_increase_value = 0
        insu_increases_for_every_year = int(
            request.POST.get("insu_increases_for_every_year")
        )
        if request.POST.get("ammortization_years"):
            ammortization_years = int(request.POST.get("ammortization_years"))
        else:
            ammortization_years = 0
        ammortization_years = ammortization_years * 12
        if request.POST.get("annual_rate_interests"):
            annual_rate_interests = float(request.POST.get("annual_rate_interests"))
        else:
            annual_rate_interests = 0
        if amount_down_payment_type == 0:
            amount_down_payment = balance * 0.01 * amount_down_payment_value
        else:
            amount_down_payment = int(amount_down_payment_value)
        if lease_rate_type == 0:
            gross_income = sft_leased * lease_rate
        else:
            gross_income = lease_rate * 12
        if gross_income:
            residential_data["dynamic_input_update"]["gross_income"] = gross_income

        noi = int(gross_income) - int(gross_income) * 0.01
        if noi:
            residential_data["dynamic_input_update"]["noi"] = noi
        if balance:
            cap_rate = noi / balance * 100
        else:
            cap_rate = 0
        if cap_rate:
            residential_data["dynamic_input_update"]["cap_rate"] = round(cap_rate, 2)

        if amount_down_payment != None:
            residential_data["dynamic_input_update"][
                "amount_down_payment"
            ] = amount_down_payment
            residential_data["dynamic_input_update"]["mortgage_loan"] = (
                balance - amount_down_payment
            )
            mortgage_loan = balance - amount_down_payment
        interestRate = 0.036
        if request.POST.get("no_years"):
            terms = int(request.POST.get("no_years"))
        else:
            terms = 0
        balVal = validateInputs(balance)
        intrVal = validateInputs(interestRate)
        if balVal and intrVal:
            amort_data, amort_dynamic_input_update = amort(
                request,
                lease_rate_type,
                amount_down_payment,
                insurance_expense,
                insu_ye_mo,
                insu_frequency,
                insu_increases_type,
                insu_increase_value,
                insu_increases_for_every_year,
                mortgage_loan,
                expense_hoa,
                hoa_ye_mo,
                hoa_frequency,
                hoa_increases_type,
                hoa_increase_value,
                hoa_increases_for_every_year,
                expense_taxes,
                taxes_ye_mo,
                taxes_frequency,
                taxes_increases_type,
                taxes_increase_value,
                taxes_increases_for_every_year,
                expense_maintenance,
                expense_vacancy,
                property_mgmt,
                lease_rate,
                sft_leased,
                closing_expenses,
                closing_concession,
                balance,
                interestRate,
                terms,
                property_mgmt_type,
                expense_vacancy_type,
                expense_maintenance_type,
                annual_rate_interests,
                ammortization_years,
            )
        residential_data["invest_analysis_html"] = amort_data
        residential_data["dynamic_input_update"].update(amort_dynamic_input_update)
        amort1_data, amort1_dynamic_input_update = amort1(
            request,
            terms,
            asset_appraisal_type,
            asset_appraisal_value,
            sales_expense_type,
            sales_expense_value,
            balance,
            amount_down_payment,
            annual_rate_interests,
            ammortization_years,
        )
        residential_data["invest_summary_html"] = amort1_data
        residential_data["dynamic_input_update"].update(amort1_dynamic_input_update)
    else:
        error = "Please Check your inputs and retry - invalid values."

    # #print(residential_data)
    return JsonResponse(residential_data)


def save_residential_reports(request):
    # print(request.POST)
    user = Users.objects.get(email="prathap.r@paccore.com")
    taxes_increases_type_final = ""
    taxes_increase_value_final = ""
    taxes_increases_for_every_year_final = ""
    taxes_increases_type = request.POST.getlist("taxes_increases_type")
    taxes_increase_value = request.POST.getlist("taxes_increase_value")
    taxes_increases_for_every_year = request.POST.getlist(
        "taxes_increases_for_every_year"
    )
    taxes_count = len(taxes_increase_value)
    if taxes_count > 0:
        for i in range(0, taxes_count):
            if taxes_increase_value[i].strip() != "":
                taxes_increases_type_final += taxes_increases_type[i] + "-"
                taxes_increase_value_final += taxes_increase_value[i] + "-"
                taxes_increases_for_every_year_final += (
                    taxes_increases_for_every_year[i] + "-"
                )
    insu_increases_type_final = ""
    insu_increase_value_final = ""
    insu_increases_for_every_year_final = ""
    insu_increases_type = request.POST.getlist("insu_increases_type")
    insu_increase_value = request.POST.getlist("insu_increase_value")
    insu_increases_for_every_year = request.POST.getlist(
        "insu_increases_for_every_year"
    )
    insu_count = len(insu_increase_value)
    if insu_count > 0:
        for i in range(0, insu_count):
            if insu_increase_value[i].strip() != "":
                insu_increases_type_final += insu_increases_type[i] + "-"
                insu_increase_value_final += insu_increase_value[i] + "-"
                insu_increases_for_every_year_final += (
                    insu_increases_for_every_year[i] + "-"
                )

    hoa_increases_type_final = ""
    hoa_increase_value_final = ""
    hoa_increases_for_every_year_final = ""
    hoa_increases_type = request.POST.getlist("hoa_increases_type")
    hoa_increase_value = request.POST.getlist("hoa_increase_value")
    hoa_increases_for_every_year = request.POST.getlist("hoa_increases_for_every_year")
    hoa_count = len(hoa_increase_value)
    if hoa_count > 0:
        for i in range(0, hoa_count):
            if hoa_increase_value[i].strip() != "":
                hoa_increases_type_final += hoa_increases_type[i] + "-"
                hoa_increase_value_final += hoa_increase_value[i] + "-"
                hoa_increases_for_every_year_final += (
                    hoa_increases_for_every_year[i] + "-"
                )
    if request.POST.get("report_id"):
        report_id = request.POST.get("report_id")
        report = Reports.objects.filter(id=int(report_id)).update(
            analysis_type=request.POST.get("analysis_type"),
            original_purchase_price=int(
                getNum(request.POST.get("original_purchase_price"))
            ),
            mortgage_loan=int(float(getNum(request.POST.get("mortgage_loan")))),
            no_years=request.POST.get("no_years"),
            amount_down_payment=int(
                float(getNum(request.POST.get("amount_down_payment")))
            ),
            ammortization_years=int(
                float(getNum(request.POST.get("ammortization_years")))
            ),
            annual_rate_interests=request.POST.get("annual_rate_interests"),
            avg_exp=int(float(getNum(request.POST.get("avg_exp")))),
            noi=int(float(getNum(request.POST.get("noi")))),
            cap_rate=int(float(getNum(request.POST.get("cap_rate")))),
            expense_taxes=int(float(getNum(request.POST.get("expense_taxes")))),
            taxes_ye_mo=request.POST.get("taxes_ye_mo"),
            taxes_frequency=request.POST.get("taxes_frequency"),
            taxes_increases_type=taxes_increases_type_final,
            taxes_increase_value=taxes_increase_value_final,
            taxes_increases_for_every_year=taxes_increases_for_every_year_final,
            expense_hoa=int(float(getNum(request.POST.get("expense_hoa")))),
            hoa_ye_mo=request.POST.get("hoa_ye_mo"),
            hoa_frequency=request.POST.get("hoa_frequency"),
            hoa_increases_type=hoa_increases_type_final,
            hoa_increase_value=hoa_increase_value_final,
            hoa_increases_for_every_year=hoa_increases_for_every_year_final,
            gross_income=int(float(getNum(request.POST.get("gross_income")))),
            expense_vacancy=int(float(getNum(request.POST.get("expense_vacancy")))),
            property_mgmt=int(float(getNum(request.POST.get("property_mgmt")))),
            expense_vacancy_type=request.POST.get("expense_vacancy_type"),
            property_mgmt_type=request.POST.get("property_mgmt_type"),
            expense_maintenance_type=request.POST.get("expense_maintenance_type"),
            expense_maintenance=int(
                float(getNum(request.POST.get("expense_maintenance")))
            ),
            debt_service_ratio=request.POST.get("debt_service_ratio"),
            amount_down_payment_value=int(
                float(getNum(request.POST.get("amount_down_payment_value")))
            ),
            amount_down_payment_type=request.POST.get("amount_down_payment_type"),
            total_sft=request.POST.get("total_sft"),
            no_units=request.POST.get("no_units"),
            asset_appraisal_type=request.POST.get("asset_appraisal_type"),
            asset_appraisal_value=int(
                float(getNum(request.POST.get("asset_appraisal_value")))
            ),
            sales_expense_type=request.POST.get("sales_expense_type"),
            sales_expense_value=int(
                float(getNum(request.POST.get("sales_expense_value")))
            ),
            insurance_expense=int(float(getNum(request.POST.get("insurance_expense")))),
            insu_ye_mo=request.POST.get("insu_ye_mo"),
            insu_frequency=request.POST.get("insu_frequency"),
            insu_increases_type=insu_increases_type_final,
            insu_increase_value=insu_increase_value_final,
            insu_increases_for_every_year=insu_increases_for_every_year_final,
            year1_roi=request.POST.get("year1_roi"),
            total_roi_percentage=request.POST.get("total_roi_percentage"),
            total_roi=request.POST.get("total_roi"),
            cloned=0,
            updated_at=datetime.now(),
        )
        if request.POST.get("tenant_id"):
            tenant_ids = request.POST.getlist("tenant_id")
            for i, tenant_id in enumerate(tenant_ids):
                tenant_name_edit = request.POST.getlist("tenant_name_edit")
                lease_rate_edit = request.POST.getlist("lease_rate_edit")
                sft_leased_edit = request.POST.getlist("sft_leased_edit")
                rent_frequency_edit = request.POST.getlist("rent_frequency_edit")
                lease_rate_type_edit = request.POST.getlist("lease_rate_type_edit")
                rent_increases_edit = request.POST.getlist(
                    "rent_increases_edit[" + str(i) + "]"
                )
                rent_increase_value_edit = request.POST.getlist(
                    "rent_increase_value_edit[" + str(i) + "]"
                )
                rent_increases_for_every_year_edit = request.POST.getlist(
                    "rent_increases_for_every_year_edit[" + str(i) + "]"
                )
                rent_increases_final = ""
                rent_increase_value_final = ""
                rent_increases_for_every_year_final = ""

                for j in range(0, len(rent_increases_edit)):
                    rent_increases_final += rent_increases_edit[j] + "-"
                    rent_increase_value_final += rent_increase_value_edit[j] + "-"
                    rent_increases_for_every_year_final += (
                        rent_increases_for_every_year_edit[j] + "-"
                    )
                affected = Tenants.objects.filter(id=tenant_id).update(
                    tenant_name=tenant_name_edit[i],
                    lease_rate=lease_rate_edit[i],
                    lease_rate_type=lease_rate_type_edit[i],
                    rent_frequency=rent_frequency_edit[i],
                    sft_leased=sft_leased_edit[i],
                    rent_increases=rent_increases_final,
                    rent_increase_value=rent_increase_value_final,
                    rent_increases_for_every_year=rent_increases_for_every_year_final,
                )

        if request.POST.get("tenant_name"):
            tenant_name = request.POST.getlist("tenant_name")
            lease_rate = request.POST.getlist("lease_rate")
            sft_leased = request.POST.getlist("sft_leased")
            rent_frequency = request.POST.getlist("rent_frequency")
            lease_rate_type = request.POST.getlist("lease_rate_type")
            tenant_nums = request.POST.get("tenant_nums").split(",")
            tenant_count = len(tenant_name)
            if tenant_count > 0:
                for i in range(0, tenant_count):
                    rent_increases = removeempty(
                        request.POST.getlist(
                            "rent_increases[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increase_value = removeempty(
                        request.POST.getlist(
                            "rent_increase_value[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "rent_increases_for_every_year[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increases_final = ""
                    rent_increase_value_final = ""
                    rent_increases_for_every_year_final = ""
                    if tenant_name[i].strip() != "":
                        for j in range(0, len(rent_increases)):
                            rent_increases_final += rent_increases[j] + "-"
                            rent_increase_value_final += rent_increase_value[j] + "-"
                            rent_increases_for_every_year_final += (
                                rent_increases_for_every_year[j] + "-"
                            )
                        tenant = Tenants.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            tenant_name=tenant_name[i],
                            lease_rate=lease_rate[i],
                            lease_rate_type=lease_rate_type[i],
                            rent_frequency=rent_frequency[i],
                            sft_leased=sft_leased[i],
                            rent_increases=rent_increases_final,
                            rent_increase_value=rent_increase_value_final,
                            rent_increases_for_every_year=rent_increases_for_every_year_final,
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        if request.POST.get("additional_expense_id").strip():
            expense_head_ids = request.POST.getlist("additional_expense_id")
            # print("expense_head_ids", expense_head_ids)
            for i, additional_expense_id in enumerate(expense_head_ids):
                expense_head_name_edit = request.POST.getlist("expense_head_name_edit")
                expense_amount_edit = request.POST.getlist("expense_amount_edit")
                expense_frequency_edit = request.POST.getlist("expense_frequency_edit")
                expense_increases_type_edit = request.POST.getlist(
                    "expense_increases_type_edit[" + str(i) + "]"
                )
                expense_increase_value_edit = request.POST.getlist(
                    "expense_increase_value_edit[" + str(i) + "]"
                )
                expense_increases_for_every_year_edit = request.POST.getlist(
                    "expense_increases_for_every_year_edit[" + str(i) + "]"
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                for j in range(0, len(expense_increases_type_edit)):
                    expense_increases_final += expense_increases_type_edit[j] + "-"
                    expense_increase_value_final += expense_increase_value_edit[j] + "-"
                    expense_increases_for_every_year_final += (
                        expense_increases_for_every_year_edit[j] + "-"
                    )

                affected = Subheads.objects.filter(
                    id=int(additional_expense_id)
                ).update(
                    report_id=int(request.POST.get("report_id")),
                    title=expense_head_name_edit[i],
                    amount=int(float(getNum(expense_amount_edit[i]))),
                    increases_type=expense_increases_final,
                    increase_value=expense_increase_value_final,
                    frequency=expense_frequency_edit[i],
                    increases_for_every_year=expense_increases_for_every_year_final,
                    type="expense",
                )

        if request.POST.get("expense_head_name"):
            expense_head_name = request.POST.getlist("expense_head_name")
            expense_amount = request.POST.getlist("expense_amount")
            frequency = request.POST.getlist("expense_frequency")
            additional_expenses_nums = request.POST.get(
                "additional_expenses_nums"
            ).split(",")
            expense_head_count = len(expense_head_name)
            if expense_head_count > 0:
                for i in range(0, expense_head_count):
                    increases_type = removeempty(
                        request.POST.getlist(
                            "expense_increases_type["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    increase_value = removeempty(
                        request.POST.getlist(
                            "expense_increase_value["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "expense_increases_for_every_year["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    expense_increases_final = ""
                    expense_increase_value_final = ""
                    expense_increases_for_every_year_final = ""
                    for j in range(len(increases_type)):
                        expense_increases_final += increases_type[j] + "-"
                        expense_increase_value_final += increase_value[j] + "-"
                        expense_increases_for_every_year_final += (
                            increases_for_every_year[j] + "-"
                        )
                    if expense_head_name[i].strip() != "":
                        subhead = Subheads.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            title=expense_head_name[i],
                            amount=int(float(getNum(expense_amount[i]))),
                            increases_type=expense_increases_final,
                            increase_value=expense_increase_value_final,
                            frequency=frequency[i],
                            increases_for_every_year=expense_increases_for_every_year_final,
                            type="expense",
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        if request.POST.get("additional_income_id"):
            additional_income_ids = request.POST.getlist("additional_income_id")
            for i, additional_income_id in enumerate(additional_income_ids):
                expense_head_name_edit = request.POST.getlist("expense_head_name_edit")
                expense_amount_edit = request.POST.getlist("expense_amount_edit")
                expense_frequency_edit = request.POST.getlist("expense_frequency_edit")
                expense_increases_type_edit = request.POST.getlist(
                    "expense_increases_type_edit[" + str(i) + "]"
                )
                expense_increase_value_edit = request.POST.getlist(
                    "expense_increase_value_edit[" + str(i) + "]"
                )
                expense_increases_for_every_year_edit = request.POST.getlist(
                    "expense_increases_for_every_year_edit[" + str(i) + "]"
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                income_name_edit = request.POST.getlist("income_name_edit")
                income_amount_edit = request.POST.getlist("income_amount_edit")
                income_frequency_edit = request.POST.getlist("income_frequency_edit")
                income_increases_type_edit = request.POST.getlist(
                    "income_increases_type_edit[" + str(i) + "]"
                )
                income_increase_value_edit = request.POST.getlist(
                    "income_increase_value_edit[" + str(i) + "]"
                )
                income_increases_for_every_year_edit = request.POST.getlist(
                    "income_increases_for_every_year_edit[" + str(i) + "]"
                )
                income_increases_final = ""
                income_increase_value_final = ""
                income_increases_for_every_year_final = ""
                for j in range(0, len(income_increases_type_edit)):
                    income_increases_final += income_increases_type_edit[j] + "-"
                    income_increase_value_final += income_increase_value_edit[j] + "-"
                    income_increases_for_every_year_final += (
                        income_increases_for_every_year_edit[j] + "-"
                    )

                affected = Subheads.objects.filter(id=additional_income_id).update(
                    report_id=int(request.POST.get("report_id")),
                    title=income_name_edit[i],
                    amount=int(float(getNum(income_amount_edit[i]))),
                    increases_type=income_increases_final,
                    increase_value=income_increase_value_final,
                    frequency=income_frequency_edit[i],
                    increases_for_every_year=income_increases_for_every_year_final,
                    type="income",
                )

        if request.POST.get("income_name"):
            income_name = request.POST.getlist("income_name")
            income_amount = request.POST.getlist("income_amount")
            frequency = request.POST.getlist("income_frequency")
            additional_income_nums = request.POST.get("additional_income_nums").split(
                ","
            )
            income_name_count = len(income_name)
            if income_name_count > 0:
                for i in range(0, income_name_count):
                    increases_type = removeempty(
                        request.POST.getlist(
                            "income_increases_type["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    increase_value = removeempty(
                        request.POST.getlist(
                            "income_increase_value["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "income_increases_for_every_year["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    income_increases_final = ""
                    income_increase_value_final = ""
                    income_increases_for_every_year_final = ""
                    for j in range(0, len(increases_type)):
                        income_increases_final += increases_type[j] + "-"
                        income_increase_value_final += increase_value[j] + "-"
                        income_increases_for_every_year_final += (
                            increases_for_every_year[j] + "-"
                        )

                    if income_name[i].strip() != "":
                        subhead = Subheads.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            title=income_name[i],
                            amount=int(float(getNum(income_amount[i]))),
                            increases_type=income_increases_final,
                            increase_value=income_increase_value_final,
                            frequency=frequency[i],
                            increases_for_every_year=income_increases_for_every_year_final,
                            type="income",
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        closing_expensename = request.POST.get("closing_expensename")
        closing_expenseamount = request.POST.get("closing_expenseamount")
        affected = Subheads.objects.filter(
            report_id=request.POST.get("report_id"), type="closing_expense"
        ).update(
            title=closing_expensename, amount=int(float(getNum(closing_expenseamount)))
        )

        closing_consession_name = request.POST.get("closing_consession_name")
        closing_consessionamount = request.POST.get("closing_consessionamount")
        affected = Subheads.objects.filter(
            report_id=request.POST.get("report_id"), type="closing_consession"
        ).update(
            title=closing_consession_name,
            amount=int(float(getNum(closing_consessionamount))),
        )
        url = "%s?id=%s" % (
            reverse("userapp:residential"),
            str(request.POST.get("report_id")).strip(),
        )
        return redirect(url)

    else:
        report = Reports.objects.create(
            user_id=user.id,
            asset_name=request.POST.get("asset_name"),
            analysis_type=request.POST.get("analysis_type"),
            acquired_on=request.POST.get("acquired_on"),
            original_purchase_price=int(
                getNum(request.POST.get("original_purchase_price"))
            ),
            closing_concession=0,
            mortgage_loan=int(float(getNum(request.POST.get("mortgage_loan")))),
            no_years=request.POST.get("no_years"),
            amount_down_payment=int(
                float(getNum(request.POST.get("amount_down_payment")))
            ),
            ammortization_years=int(
                float(getNum(request.POST.get("ammortization_years")))
            ),
            annual_rate_interests=request.POST.get("annual_rate_interests"),
            avg_exp=int(float(getNum(request.POST.get("avg_exp")))),
            noi=int(float(getNum(request.POST.get("noi")))),
            cap_rate=int(float(getNum(request.POST.get("cap_rate")))),
            closing_expenses=0,
            expense_taxes=int(float(getNum(request.POST.get("expense_taxes")))),
            taxes_ye_mo=request.POST.get("taxes_ye_mo"),
            taxes_frequency=request.POST.get("taxes_frequency"),
            taxes_increases_type=taxes_increases_type_final,
            taxes_increase_value=taxes_increase_value_final,
            taxes_increases_for_every_year=taxes_increases_for_every_year_final,
            expense_hoa=int(float(getNum(request.POST.get("expense_hoa")))),
            hoa_ye_mo=request.POST.get("hoa_ye_mo"),
            hoa_frequency=request.POST.get("hoa_frequency"),
            hoa_increases_type=hoa_increases_type_final,
            hoa_increase_value=hoa_increase_value_final,
            hoa_increases_for_every_year=hoa_increases_for_every_year_final,
            gross_income=int(float(getNum(request.POST.get("gross_income")))),
            expense_vacancy=int(float(getNum(request.POST.get("expense_vacancy")))),
            property_mgmt=int(float(getNum(request.POST.get("property_mgmt")))),
            expense_vacancy_type=request.POST.get("expense_vacancy_type"),
            property_mgmt_type=request.POST.get("property_mgmt_type"),
            expense_maintenance_type=request.POST.get("expense_maintenance_type"),
            expense_maintenance=int(
                float(getNum(request.POST.get("expense_maintenance")))
            ),
            debt_service_ratio=request.POST.get("debt_service_ratio"),
            amount_down_payment_value=int(
                float(getNum(request.POST.get("amount_down_payment_value")))
            ),
            amount_down_payment_type=request.POST.get("amount_down_payment_type"),
            total_sft=request.POST.get("total_sft"),
            no_units=request.POST.get("no_units"),
            asset_appraisal_type=request.POST.get("asset_appraisal_type"),
            asset_appraisal_value=int(
                float(getNum(request.POST.get("asset_appraisal_value")))
            ),
            sales_expense_type=request.POST.get("sales_expense_type"),
            sales_expense_value=int(
                float(getNum(request.POST.get("sales_expense_value")))
            ),
            insurance_expense=int(float(getNum(request.POST.get("insurance_expense")))),
            insu_ye_mo=request.POST.get("insu_ye_mo"),
            insu_frequency=request.POST.get("insu_frequency"),
            insu_increases_type=insu_increases_type_final,
            insu_increase_value=insu_increase_value_final,
            insu_increases_for_every_year=insu_increases_for_every_year_final,
            year1_roi=request.POST.get("year1_roi"),
            total_roi_percentage=request.POST.get("total_roi_percentage"),
            total_roi=request.POST.get("total_roi"),
            cloned=0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        tenant_name = request.POST.getlist("tenant_name")
        lease_rate = request.POST.getlist("lease_rate")
        sft_leased = request.POST.getlist("sft_leased")
        rent_frequency = request.POST.getlist("rent_frequency")
        lease_rate_type = request.POST.getlist("lease_rate_type")
        tenant_nums = request.POST.get("tenant_nums").split(",")
        tenant_count = len(tenant_name)
        if tenant_count > 0:
            for i in range(0, tenant_count):
                rent_increases = removeempty(
                    request.POST.getlist("rent_increases[" + str(tenant_nums[i]) + "]")
                )
                rent_increase_value = removeempty(
                    request.POST.getlist(
                        "rent_increase_value[" + str(tenant_nums[i]) + "]"
                    )
                )
                rent_increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "rent_increases_for_every_year[" + str(tenant_nums[i]) + "]"
                    )
                )
                rent_increases_final = ""
                rent_increase_value_final = ""
                rent_increases_for_every_year_final = ""
                if tenant_name[i].strip() != "":
                    for j in range(0, len(rent_increases)):
                        rent_increases_final += rent_increases[j] + "-"
                        rent_increase_value_final += rent_increase_value[j] + "-"
                        rent_increases_for_every_year_final += (
                            rent_increases_for_every_year[j] + "-"
                        )
                    tenant = Tenants.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        tenant_name=tenant_name[i],
                        lease_rate=lease_rate[i],
                        lease_rate_type=lease_rate_type[i],
                        rent_frequency=rent_frequency[i],
                        sft_leased=sft_leased[i],
                        rent_increases=rent_increases_final,
                        rent_increase_value=rent_increase_value_final,
                        rent_increases_for_every_year=rent_increases_for_every_year_final,
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        expense_head_name = request.POST.getlist("expense_head_name")
        expense_amount = request.POST.getlist("expense_amount")
        frequency = request.POST.getlist("expense_frequency")
        additional_expenses_nums = request.POST.get("additional_expenses_nums").split(
            ","
        )
        expense_head_count = len(expense_head_name)
        if expense_head_count > 0:
            for i in range(0, expense_head_count):
                increases_type = removeempty(
                    request.POST.getlist(
                        "expense_increases_type["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                increase_value = removeempty(
                    request.POST.getlist(
                        "expense_increase_value["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "expense_increases_for_every_year["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                for j in range(len(increases_type)):
                    expense_increases_final += increases_type[j] + "-"
                    expense_increase_value_final += increase_value[j] + "-"
                    expense_increases_for_every_year_final += (
                        increases_for_every_year[j] + "-"
                    )
                if expense_head_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=expense_head_name[i],
                        amount=int(float(getNum(expense_amount[i]))),
                        increases_type=expense_increases_final,
                        increase_value=expense_increase_value_final,
                        frequency=frequency[i],
                        increases_for_every_year=expense_increases_for_every_year_final,
                        type="expense",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        income_name = request.POST.getlist("income_name")
        income_amount = request.POST.getlist("income_amount")
        frequency = request.POST.getlist("income_frequency")
        additional_income_nums = request.POST.get("additional_income_nums").split(",")
        income_name_count = len(income_name)
        if income_name_count > 0:
            for i in range(0, income_name_count):
                increases_type = removeempty(
                    request.POST.getlist(
                        "income_increases_type[" + str(additional_income_nums[i]) + "]"
                    )
                )
                increase_value = removeempty(
                    request.POST.getlist(
                        "income_increase_value[" + str(additional_income_nums[i]) + "]"
                    )
                )
                increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "income_increases_for_every_year["
                        + str(additional_income_nums[i])
                        + "]"
                    )
                )
                income_increases_final = ""
                income_increase_value_final = ""
                income_increases_for_every_year_final = ""
                for j in range(0, len(increases_type)):
                    income_increases_final += increases_type[j] + "-"
                    income_increase_value_final += increase_value[j] + "-"
                    income_increases_for_every_year_final += (
                        increases_for_every_year[j] + "-"
                    )

                if income_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=income_name[i],
                        amount=int(float(getNum(income_amount[i]))),
                        increases_type=income_increases_final,
                        increase_value=income_increase_value_final,
                        frequency=frequency[i],
                        increases_for_every_year=income_increases_for_every_year_final,
                        type="income",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        closing_expensename = request.POST.getlist("closing_expensename")
        closing_expenseamount = request.POST.getlist("closing_expenseamount")
        closing_expensename_count = len(closing_expensename)
        if closing_expensename_count > 0:
            for i in range(0, closing_expensename_count):
                if closing_expensename[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=closing_expensename[i],
                        amount=int(float(getNum(closing_expenseamount[i]))),
                        type="closing_expense",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        closing_consession_name = request.POST.getlist("closing_consession_name")
        closing_consessionamount = request.POST.getlist("closing_consessionamount")
        closing_consession_name_count = len(closing_consession_name)
        if closing_consession_name_count > 0:
            for i in range(0, closing_consession_name_count):
                if closing_consession_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=closing_consession_name[i],
                        amount=int(float(getNum(closing_consessionamount[i]))),
                        type="closing_consession",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        url = "%s?id=%s" % (reverse("userapp:residential"), str(report.id))
        return redirect(url)
        # return HttpResponse("<h1>Saved Residential Reports</h1>")


###########Commercial DSCR###################


def comm_dscr(request):
    data = {}
    if request.GET.get("id"):
        dscr_id = int(request.GET.get("id"))
        reportsdata = Dscrs.objects.filter(id=dscr_id).first()
        data["reportsdata"] = reportsdata
    else:
        data["reportsdata"] = ""

    return render(request, "comm_dscr.html", data)


def comm_dscr_analysis(request):
    comm_dscr_data = {}
    comm_dscr_data["dynamic_input_update"] = {}
    property_value = float(getNum(request.POST.get("property_value")))
    annual_operating_exp = float(request.POST.get("annual_operating_exp"))
    mgmt_fees = float(getNum(request.POST.get("mgmt_fees")))
    loan_amount_check = property_value * 0.25
    approximate_sq_footage = float(getNum(request.POST.get("approximate_sq_footage")))
    property_type = request.POST.get("property_type")
    no_units = float(getNum(request.POST.get("no_units")))
    interest_rate = float(getNum(request.POST.get("interest_rate")))
    gross_annual_rental = float(getNum(request.POST.get("gross_annual_rental")))
    other_income = getNum(request.POST.get("other_income"))
    total_annual_rents = int(gross_annual_rental) + int(other_income)
    less_vacancy = (
        total_annual_rents * 0.05
    )  # added this line to not get any error when no property type is given, check and remove later if not correct.
    if property_type == "Retail":
        less_vacancy = total_annual_rents * 0.05
    if property_type == "Multi-Family":
        less_vacancy = total_annual_rents * 0.05
    if property_type == "Mixed-Use":
        less_vacancy = total_annual_rents * 0.05
    if property_type == "Industrial":
        less_vacancy = total_annual_rents * 0.05
    if property_type == "Office":
        less_vacancy = total_annual_rents * 0.10

    comm_dscr_data["dynamic_input_update"]["less_vacancy"] = getNum(less_vacancy)
    comm_dscr_data["dynamic_input_update"]["total_annual_rents"] = getNum(
        total_annual_rents
    )
    effective_total_annual_rents = total_annual_rents - less_vacancy
    comm_dscr_data["dynamic_input_update"]["effective_total_annual_rents"] = getNum(
        effective_total_annual_rents
    )
    utilities_telephone = getNum(request.POST.get("utilities_telephone"))
    repairs_maintenance = getNum(request.POST.get("repairs_maintenance"))
    salaries_legal = getNum(request.POST.get("salaries_legal"))
    snow_trash = getNum(request.POST.get("snow_trash"))
    re_taxes = getNum(request.POST.get("re_taxes"))
    insurance = getNum(request.POST.get("insurance"))
    other_operating_exp = getNum(request.POST.get("other_operating_exp"))
    total_operating_expenses = (
        int(utilities_telephone)
        + int(repairs_maintenance)
        + int(salaries_legal)
        + int(snow_trash)
        + int(re_taxes)
        + int(insurance)
        + int(other_operating_exp)
        + int(mgmt_fees)
        + int(annual_operating_exp)
    )
    comm_dscr_data["dynamic_input_update"]["total_operating_expenses"] = getNum(
        total_operating_expenses
    )
    less_reserves = (
        approximate_sq_footage * 0.15
    )  # added this line to not get any error when no property type is given, check and remove later if not correct.
    if property_type == "Retail":
        less_reserves = approximate_sq_footage * 0.15
    if property_type == "Multi-Family":
        less_reserves = no_units * 250
    if property_type == "Mixed-Use":
        less_reserves = no_units * 250
    if property_type == "Industrial":
        less_reserves = approximate_sq_footage * 0.15
    if property_type == "Office":
        less_reserves = approximate_sq_footage * 0.2
    comm_dscr_data["dynamic_input_update"]["less_reserves"] = getNum(less_reserves)
    cash_flow = effective_total_annual_rents - total_operating_expenses - less_reserves
    ADS = cash_flow / 1.25
    monthly_loan_payment = ADS / 12
    amortization_years = float(getNum(request.POST.get("amortization_years")))
    interest_rate = interest_rate * 0.01
    ir = interest_rate / 12
    np = amortization_years * 12
    loan_amount = PV(ir, np, monthly_loan_payment)
    monthly_loan_payment_prev = round(monthly_loan_payment, 0)
    comm_dscr_data["dynamic_input_update"]["monthly_loan_payment_prev"] = getNum(
        monthly_loan_payment_prev
    )
    comm_dscr_data["dynamic_input_update"]["loan_amount"] = getNum(loan_amount)
    downpayment_val = property_value - loan_amount
    comm_dscr_data["dynamic_input_update"]["downpayment_val"] = getNum(downpayment_val)
    try:
        ltv = getNum(loan_amount / property_value) * 100
    except ZeroDivisionError:
        ltv = 0
    comm_dscr_data["dynamic_input_update"]["ltv"] = getNum(ltv)
    ltv = round(ltv, 2)
    if ltv > 75:
        down_revised = round((property_value * 0.25), 0)
        comm_dscr_data["dynamic_input_update"]["down_revised"] = getNum(down_revised)
        floan_amount = property_value - down_revised
        comm_dscr_data["dynamic_input_update"]["floan_amount"] = getNum(floan_amount)
        comm_dscr_data["dynamic_input_update"]["ltv"] = 75
        ltv = 75

    comm_dscr_data["dynamic_input_update"]["ADS"] = getNum(ADS)
    comm_dscr_data["dynamic_input_update"]["cash_flow"] = getNum(cash_flow)
    comm_dscr_data["dynamic_input_update"]["cash_flow"] = getNum(cash_flow)

    cash_flow_after_debt_service = cash_flow - ADS
    comm_dscr_data["dynamic_input_update"]["cash_flow_after_debt_service"] = getNum(
        cash_flow_after_debt_service
    )
    try:
        debt_service_coverage_ratio = cash_flow / ADS
    except ZeroDivisionError:
        debt_service_coverage_ratio = 0
    comm_dscr_data["dynamic_input_update"]["debt_service_coverage_ratio"] = getNum(
        debt_service_coverage_ratio
    )
    try:
        cash_flow_per = (cash_flow / total_annual_rents) * 100
    except ZeroDivisionError:
        cash_flow_per = 0
    try:
        total_operating_expenses_per = (gross_annual_rental / total_annual_rents) * 100
    except ZeroDivisionError:
        total_operating_expenses_per = 0
    try:
        total_annual_rents_per = (total_operating_expenses / total_annual_rents) * 100
    except ZeroDivisionError:
        total_annual_rents_per = 0

    return JsonResponse(comm_dscr_data)


def save_comm_dscr_reports(request):
    # print(request.POST)
    user = Users.objects.get(email="prathap.r@paccore.com")
    try:
        down_payment_percentage = (
            float(getNum(request.POST.get("down_payment")))
            / float(getNum(request.POST.get("property_value")))
        ) * 100
    except ZeroDivisionError:
        down_payment_percentage = 0
    down_payment_percentage = round(down_payment_percentage, 2)
    if request.POST.get("report_id"):
        report_id = int(request.POST.get("report_id"))
        affected = Dscrs.objects.filter(id=report_id).update(
            borrower_name=request.POST.get("borrower_name"),
            property_type=request.POST.get("property_type"),
            no_units=int(float(getNum(request.POST.get("no_units")))),
            approximate_sq_footage=int(
                float(getNum(request.POST.get("approximate_sq_footage")))
            ),
            loan_amount=int(float(getNum(request.POST.get("loan_amount")))),
            property_value=int(float(getNum(request.POST.get("property_value")))),
            ltv=int(float(getNum(request.POST.get("ltv")))),
            amortization_years=int(
                float(getNum(request.POST.get("amortization_years")))
            ),
            interest_rate=float(getNum(request.POST.get("interest_rate"))),
            down_payment=int(float(getNum(request.POST.get("down_payment")))),
            gross_annual_rental=int(
                float(getNum(request.POST.get("gross_annual_rental")))
            ),
            other_income=int(float(getNum(request.POST.get("other_income")))),
            utilities_telephone=int(
                float(getNum(request.POST.get("utilities_telephone")))
            ),
            down_payment_percentage=request.POST.get("down_payment_percentage"),
            repairs_maintenance=int(
                float(getNum(request.POST.get("repairs_maintenance")))
            ),
            salaries_legal=int(float(getNum(request.POST.get("salaries_legal")))),
            snow_trash=int(float(getNum(request.POST.get("snow_trash")))),
            re_taxes=int(float(getNum(request.POST.get("re_taxes")))),
            insurance=int(float(getNum(request.POST.get("insurance")))),
            dscr_ratio=request.POST.get("dscr_ratio"),
            mgmt_fees=int(float(getNum(request.POST.get("mgmt_fees")))),
            annual_operating_exp=int(
                float(getNum(request.POST.get("annual_operating_exp")))
            ),
            other_operating_exp=int(
                float(getNum(request.POST.get("other_operating_exp")))
            ),
            cloned=0,
            updated_at=datetime.now(),
        )
        url = "%s?id=%s" % (
            reverse("userapp:comm-dscr"),
            str(request.POST.get("report_id")).strip(),
        )
        return redirect(url)
    else:
        report = Dscrs.objects.create(
            user=user,
            borrower_name=request.POST.get("borrower_name"),
            property_type=request.POST.get("property_type"),
            no_units=int(float(getNum(request.POST.get("no_units")))),
            approximate_sq_footage=int(
                float(getNum(request.POST.get("approximate_sq_footage")))
            ),
            loan_amount=int(float(getNum(request.POST.get("loan_amount")))),
            property_value=int(float(getNum(request.POST.get("property_value")))),
            ltv=int(float(getNum(request.POST.get("ltv")))),
            amortization_years=int(
                float(getNum(request.POST.get("amortization_years")))
            ),
            interest_rate=float(getNum(request.POST.get("interest_rate"))),
            down_payment=int(float(getNum(request.POST.get("down_payment")))),
            gross_annual_rental=int(
                float(getNum(request.POST.get("gross_annual_rental")))
            ),
            other_income=int(float(getNum(request.POST.get("other_income")))),
            utilities_telephone=int(
                float(getNum(request.POST.get("utilities_telephone")))
            ),
            down_payment_percentage=request.POST.get("down_payment_percentage"),
            repairs_maintenance=int(
                float(getNum(request.POST.get("repairs_maintenance")))
            ),
            salaries_legal=int(float(getNum(request.POST.get("salaries_legal")))),
            snow_trash=int(float(getNum(request.POST.get("snow_trash")))),
            re_taxes=int(float(getNum(request.POST.get("re_taxes")))),
            insurance=int(float(getNum(request.POST.get("insurance")))),
            dscr_ratio=request.POST.get("dscr_ratio"),
            mgmt_fees=int(float(getNum(request.POST.get("mgmt_fees")))),
            annual_operating_exp=int(
                float(getNum(request.POST.get("annual_operating_exp")))
            ),
            other_operating_exp=int(
                float(getNum(request.POST.get("other_operating_exp")))
            ),
            cloned=0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        # if report:
        #     wallet = Wallets.objects.create(
        #         user_id=user.id,
        #         email="",
        #         type="Debit",
        #         narration=request.POST.get("borrower_name"),
        #         amount="15",
        #         status="COMPLETED",
        #         report_id=report.id,
        #         report_type="2",
        #         transaction_id="txn".time(),
        #     )
        url = "%s?id=%s" % (reverse("userapp:comm-dscr"), str(report.id))
        return redirect(url)
        # return HttpResponse("<h1>Saved Commercial Dscr Reports</h1>")


############Commercial ROI###################


def comm_roi(request):
    data = {}
    if request.GET.get("id"):
        report_id = int(request.GET.get("id"))
        reportsdata = Reports.objects.filter(id=report_id).first()
        data["reportsdata"] = reportsdata
        tenants = Tenants.objects.filter(report_id=report_id)
        data["tenants"] = tenants
        data["tenants_count"] = tenants.count()
        additional_incomes = Subheads.objects.filter(report_id=report_id, type="income")
        data["additional_income"] = additional_incomes
        data["additional_income_count"] = additional_incomes.count()
        additional_expenses = Subheads.objects.filter(
            report_id=report_id, type="expense"
        )
        data["additional_expenses"] = additional_expenses
        data["additional_expenses_count"] = additional_expenses.count()
        data["clo_exp"] = Subheads.objects.filter(
            report_id=report_id, type="closing_expense"
        )
        data["sum_clo_conc"] = Subheads.objects.filter(
            report_id=report_id, type="closing_consession"
        ).aggregate(Sum("amount"))["amount__sum"]
        data["sum_clo_exp"] = Subheads.objects.filter(
            report_id=report_id, type="closing_expense"
        ).aggregate(Sum("amount"))["amount__sum"]
        data["clo_con"] = Subheads.objects.filter(
            report_id=report_id, type="closing_consession"
        )
        data["expenses"] = Subheads.objects.filter(report_id=report_id, type="expense")
        # print(data)
    elif request.GET.get("descr_id"):
        data["descrdata"] = Dscrs.objects.filter(
            id=int(request.GET.get("descr_id"))
        ).first()
    else:
        data["reportsdata"] = ""
    return render(request, "comm_roi.html", data)


def comm_roi_analysis(request):
    form_data = request.POST.get("form_data")
    edited_post_data = QueryDict(form_data.replace("_edit", ""))
    request.POST = edited_post_data
    # print(request.POST)
    comm_roi_data = {}
    comm_roi_data["dynamic_input_update"] = {}
    if request.POST:
        x = 0
        expense_vacancy_type = int(request.POST.get("expense_vacancy_type"))
        if request.POST.get("expense_vacancy"):
            expense_vacancy = float(request.POST.get("expense_vacancy"))
        else:
            expense_vacancy = 0
        tenant_name = request.POST.get("tenant_name")
        balance = 0
        if request.POST.get("original_purchase_price"):
            balance = float(request.POST.get("original_purchase_price"))
        closing_concession = request.POST.get("closing_consessions_view")
        if not closing_concession.strip():
            closing_concession = 0
        closing_expenses = request.POST.get("closing_expenses_view")
        if not closing_expenses.strip():
            closing_expenses = 0
        sft_leased = request.POST.get("sft_leased")
        if not sft_leased:
            sft_leased = 0
        else:
            sft_leased = int(sft_leased)
        lease_rate = request.POST.get("lease_rate")
        if not lease_rate:
            lease_rate = 0
        else:
            lease_rate = int(lease_rate)
        gross_income = request.POST.get("gross_income")
        avg_exp = float(getNum(request.POST.get("avg_exp")))
        rent_increases = request.POST.get("rent_increases")
        rent_increase_value = request.POST.get("rent_increase_value")

        amount_down_payment_type = int(request.POST.get("amount_down_payment_type"))
        if request.POST.get("amount_down_payment_value"):
            amount_down_payment_value = float(
                request.POST.get("amount_down_payment_value")
            )
        else:
            amount_down_payment_value = 0

        asset_appraisal_type = int(request.POST.get("asset_appraisal_type"))
        if request.POST.get("asset_appraisal_value"):
            asset_appraisal_value = float(request.POST.get("asset_appraisal_value"))
        else:
            asset_appraisal_value = 0
        sales_expense_type = int(request.POST.get("sales_expense_type"))
        if request.POST.get("sales_expense_value"):
            sales_expense_value = float(request.POST.get("sales_expense_value"))
        else:
            sales_expense_value = 0
        lease_rate_type = request.POST.get("lease_rate_type")
        if request.POST.get("expense_taxes"):
            expense_taxes = int(request.POST.get("expense_taxes"))
        else:
            expense_taxes = 0
        taxes_ye_mo = int(request.POST.get("taxes_ye_mo"))
        taxes_frequency = int(request.POST.get("taxes_frequency"))
        taxes_increases_type = int(request.POST.get("taxes_increases_type"))
        if request.POST.get("taxes_increase_value"):
            taxes_increase_value = int(request.POST.get("taxes_increase_value"))
        else:
            taxes_increase_value = 0
        if request.POST.get("taxes_increases_for_every_year"):
            taxes_increases_for_every_year = int(
                request.POST.get("taxes_increases_for_every_year")
            )
        else:
            taxes_increases_for_every_year = 0

        if request.POST.get("expense_hoa"):
            expense_hoa = float(request.POST.get("expense_hoa"))
        else:
            expense_hoa = 0
        hoa_ye_mo = int(request.POST.get("hoa_ye_mo"))
        hoa_frequency = int(request.POST.get("hoa_frequency"))
        hoa_increases_type = int(request.POST.get("hoa_increases_type"))
        if request.POST.get("hoa_increase_value"):
            hoa_increase_value = float(request.POST.get("hoa_increase_value"))
        else:
            hoa_increase_value = 0
        hoa_increases_for_every_year = int(
            request.POST.get("hoa_increases_for_every_year")
        )
        if request.POST.get("expense_cam"):
            expense_cam = float(request.POST.get("expense_cam"))
        else:
            expense_cam = 0
        cam_ye_mo = int(request.POST.get("cam_ye_mo"))
        cam_frequency = int(request.POST.get("cam_frequency"))
        cam_increases_type = int(request.POST.get("cam_increases_type"))
        if request.POST.get("cam_increase_value"):
            cam_increase_value = float(request.POST.get("cam_increase_value"))
        else:
            cam_increase_value = 0
        cam_increases_for_every_year = int(
            request.POST.get("cam_increases_for_every_year")
        )
        if request.POST.get("expense_management"):
            expense_management = float(request.POST.get("expense_management"))
        else:
            expense_management = 0
        management_ye_mo = int(request.POST.get("management_ye_mo"))
        management_frequency = int(request.POST.get("management_frequency"))
        management_increases_type = int(request.POST.get("management_increases_type"))
        if request.POST.get("management_increase_value"):
            management_increase_value = float(
                request.POST.get("management_increase_value")
            )
        else:
            management_increase_value = 0
        management_increases_for_every_year = int(
            request.POST.get("management_increases_for_every_year")
        )

        if request.POST.get("expense_administrative"):
            expense_administrative = float(request.POST.get("expense_administrative"))
        else:
            expense_administrative = 0
        administrative_ye_mo = int(request.POST.get("administrative_ye_mo"))
        administrative_frequency = int(request.POST.get("administrative_frequency"))
        administrative_increases_type = int(
            request.POST.get("administrative_increases_type")
        )
        if request.POST.get("administrative_increase_value"):
            administrative_increase_value = float(
                request.POST.get("administrative_increase_value")
            )
        else:
            administrative_increase_value = 0
        administrative_increases_for_every_year = int(
            request.POST.get("administrative_increases_for_every_year")
        )

        if request.POST.get("expense_utilities"):
            expense_utilities = float(request.POST.get("expense_utilities"))
        else:
            expense_utilities = 0
        utilities_ye_mo = int(request.POST.get("utilities_ye_mo"))
        utilities_frequency = int(request.POST.get("utilities_frequency"))
        utilities_increases_type = int(request.POST.get("utilities_increases_type"))
        if request.POST.get("utilities_increase_value"):
            utilities_increase_value = float(
                request.POST.get("utilities_increase_value")
            )
        else:
            utilities_increase_value = 0
        utilities_increases_for_every_year = int(
            request.POST.get("utilities_increases_for_every_year")
        )

        if request.POST.get("insurance_expense"):
            insurance_expense = float(request.POST.get("insurance_expense"))
        else:
            insurance_expense = 0
        insu_ye_mo = int(request.POST.get("insu_ye_mo"))
        insu_frequency = int(request.POST.get("insu_frequency"))
        insu_increases_type = int(request.POST.get("insu_increases_type"))
        if request.POST.get("insu_increase_value"):
            insu_increase_value = float(request.POST.get("insu_increase_value"))
        else:
            insu_increase_value = 0
        insu_increases_for_every_year = int(
            request.POST.get("insu_increases_for_every_year")
        )

        if request.POST.get("reimbursement_income"):
            reimbursement_income = float(request.POST.get("reimbursement_income"))
        else:
            reimbursement_income = 0
        reim_ye_mo = int(request.POST.get("reim_ye_mo"))
        reim_frequency = int(request.POST.get("reim_frequency"))
        reim_increases_type = int(request.POST.get("reim_increases_type"))
        if request.POST.get("reim_increase_value"):
            reim_increase_value = float(request.POST.get("reim_increase_value"))
        else:
            reim_increase_value = 0
        reim_increases_for_every_year = int(
            request.POST.get("reim_increases_for_every_year")
        )
        debt_service_ratio = request.POST.get("debt_service_ratio")
        if debt_service_ratio == "":
            debt_service_ratio = 91
        if request.POST.get("ammortization_years"):
            ammortization_years = int(request.POST.get("ammortization_years"))
        else:
            ammortization_years = 0
        ammortization_years = ammortization_years * 12
        if request.POST.get("annual_rate_interests"):
            annual_rate_interests = float(request.POST.get("annual_rate_interests"))
        else:
            annual_rate_interests = 0
        if amount_down_payment_type == 0:
            amount_down_payment = balance * 0.01 * amount_down_payment_value
        else:
            amount_down_payment = (
                int(amount_down_payment_value)
                - int(closing_concession)
                + int(closing_expenses)
            )
            amount_down_payment = int(amount_down_payment_value)
        if lease_rate_type == 0:
            gross_income = sft_leased * lease_rate
        else:
            gross_income = lease_rate * 12
        if gross_income:
            comm_roi_data["dynamic_input_update"]["gross_income"] = gross_income

        noi = int(gross_income) - int(gross_income) * 0.01
        if noi:
            comm_roi_data["dynamic_input_update"]["noi"] = noi
        if balance:
            cap_rate = noi / balance * 100
        else:
            cap_rate = 0
        if cap_rate:
            comm_roi_data["dynamic_input_update"]["cap_rate"] = round(cap_rate, 2)
        if amount_down_payment != None:
            comm_roi_data["dynamic_input_update"][
                "amount_down_payment"
            ] = amount_down_payment
            comm_roi_data["dynamic_input_update"]["mortgage_loan"] = (
                balance - amount_down_payment
            )
            mortgage_loan = balance - amount_down_payment
        interestRate = 0.036
        if request.POST.get("no_years"):
            terms = int(request.POST.get("no_years"))
        else:
            terms = 0

        balVal = validateInputs(balance)
        intrVal = validateInputs(interestRate)

        if balVal and intrVal:
            amort_data, amort_dynamic_input_update = comm_amort(
                request,
                debt_service_ratio,
                reimbursement_income,
                reim_ye_mo,
                reim_frequency,
                reim_increases_type,
                reim_increase_value,
                reim_increases_for_every_year,
                expense_administrative,
                administrative_ye_mo,
                administrative_frequency,
                administrative_increases_type,
                administrative_increase_value,
                administrative_increases_for_every_year,
                expense_management,
                management_ye_mo,
                management_frequency,
                management_increases_type,
                management_increase_value,
                management_increases_for_every_year,
                lease_rate_type,
                amount_down_payment,
                insurance_expense,
                insu_ye_mo,
                insu_frequency,
                insu_increases_type,
                insu_increase_value,
                insu_increases_for_every_year,
                mortgage_loan,
                expense_utilities,
                utilities_ye_mo,
                utilities_frequency,
                utilities_increases_type,
                utilities_increase_value,
                utilities_increases_for_every_year,
                expense_cam,
                cam_ye_mo,
                cam_frequency,
                cam_increases_type,
                cam_increase_value,
                cam_increases_for_every_year,
                expense_hoa,
                hoa_ye_mo,
                hoa_frequency,
                hoa_increases_type,
                hoa_increase_value,
                hoa_increases_for_every_year,
                expense_taxes,
                taxes_ye_mo,
                taxes_frequency,
                taxes_increases_type,
                taxes_increase_value,
                taxes_increases_for_every_year,
                avg_exp,
                lease_rate,
                sft_leased,
                closing_expenses,
                closing_concession,
                tenant_name,
                balance,
                interestRate,
                terms,
                annual_rate_interests,
                ammortization_years,
                expense_vacancy,
                expense_vacancy_type,
            )
            comm_roi_data["invest_analysis_html"] = amort_data
            comm_roi_data["dynamic_input_update"].update(amort_dynamic_input_update)
            amort1_data, amort1_dynamic_input_update = amort1(
                request,
                terms,
                asset_appraisal_type,
                asset_appraisal_value,
                sales_expense_type,
                sales_expense_value,
                balance,
                amount_down_payment,
                annual_rate_interests,
                ammortization_years,
            )
            comm_roi_data["invest_summary_html"] = amort1_data
            comm_roi_data["dynamic_input_update"].update(amort1_dynamic_input_update)
    # print(comm_roi_data)
    return JsonResponse(comm_roi_data)


def save_comm_roi_reports(request):
    # print(request.POST)
    user = Users.objects.get(email="prathap.r@paccore.com")
    taxes_increases_type_final = ""
    taxes_increase_value_final = ""
    taxes_increases_for_every_year_final = ""
    taxes_increases_type = request.POST.getlist("taxes_increases_type")
    taxes_increase_value = request.POST.getlist("taxes_increase_value")
    taxes_increases_for_every_year = request.POST.getlist(
        "taxes_increases_for_every_year"
    )
    taxes_count = len(taxes_increase_value)
    if taxes_count > 0:
        for i in range(0, taxes_count):
            if taxes_increase_value[i].strip() != "":
                taxes_increases_type_final += taxes_increases_type[i] + "-"
                taxes_increase_value_final += taxes_increase_value[i] + "-"
                taxes_increases_for_every_year_final += (
                    taxes_increases_for_every_year[i] + "-"
                )
    insu_increases_type_final = ""
    insu_increase_value_final = ""
    insu_increases_for_every_year_final = ""
    insu_increases_type = request.POST.getlist("insu_increases_type")
    insu_increase_value = request.POST.getlist("insu_increase_value")
    insu_increases_for_every_year = request.POST.getlist(
        "insu_increases_for_every_year"
    )
    insu_count = len(insu_increase_value)
    if insu_count > 0:
        for i in range(0, insu_count):
            if insu_increase_value[i].strip() != "":
                insu_increases_type_final += insu_increases_type[i] + "-"
                insu_increase_value_final += insu_increase_value[i] + "-"
                insu_increases_for_every_year_final += (
                    insu_increases_for_every_year[i] + "-"
                )

    hoa_increases_type_final = ""
    hoa_increase_value_final = ""
    hoa_increases_for_every_year_final = ""
    hoa_increases_type = request.POST.getlist("hoa_increases_type")
    hoa_increase_value = request.POST.getlist("hoa_increase_value")
    hoa_increases_for_every_year = request.POST.getlist("hoa_increases_for_every_year")
    hoa_count = len(hoa_increase_value)
    if hoa_count > 0:
        for i in range(0, hoa_count):
            if hoa_increase_value[i].strip() != "":
                hoa_increases_type_final += hoa_increases_type[i] + "-"
                hoa_increase_value_final += hoa_increase_value[i] + "-"
                hoa_increases_for_every_year_final += (
                    hoa_increases_for_every_year[i] + "-"
                )

    cam_increases_type_final = ""
    cam_increase_value_final = ""
    cam_increases_for_every_year_final = ""
    cam_increases_type = request.POST.getlist("cam_increases_type")
    cam_increase_value = request.POST.getlist("cam_increase_value")
    cam_increases_for_every_year = request.POST.getlist("cam_increases_for_every_year")
    cam_count = len(cam_increase_value)
    if cam_count > 0:
        for i in range(0, cam_count):
            if cam_increase_value[i].strip() != "":
                cam_increases_type_final += cam_increases_type[i] + "-"
                cam_increase_value_final += cam_increase_value[i] + "-"
                cam_increases_for_every_year_final += (
                    cam_increases_for_every_year[i] + "-"
                )

    utilities_increases_type_final = ""
    utilities_increase_value_final = ""
    utilities_increases_for_every_year_final = ""
    utilities_increases_type = request.POST.getlist("utilities_increases_type")
    utilities_increase_value = request.POST.getlist("utilities_increase_value")
    utilities_increases_for_every_year = request.POST.getlist(
        "utilities_increases_for_every_year"
    )
    utilities_count = len(utilities_increase_value)
    if utilities_count > 0:
        for i in range(0, utilities_count):
            if utilities_increase_value[i].strip() != "":
                utilities_increases_type_final += utilities_increases_type[i] + "-"
                utilities_increase_value_final += utilities_increase_value[i] + "-"
                utilities_increases_for_every_year_final += (
                    utilities_increases_for_every_year[i] + "-"
                )

    management_increases_type_final = ""
    management_increase_value_final = ""
    management_increases_for_every_year_final = ""
    management_increases_type = request.POST.getlist("management_increases_type")
    management_increase_value = request.POST.getlist("management_increase_value")
    management_increases_for_every_year = request.POST.getlist(
        "management_increases_for_every_year"
    )
    management_count = len(management_increase_value)
    if management_count > 0:
        for i in range(0, management_count):
            if management_increase_value[i].strip() != "":
                management_increases_type_final += management_increases_type[i] + "-"
                management_increase_value_final += management_increase_value[i] + "-"
                management_increases_for_every_year_final += (
                    management_increases_for_every_year[i] + "-"
                )

    administrative_increases_type_final = ""
    administrative_increase_value_final = ""
    administrative_increases_for_every_year_final = ""
    administrative_increases_type = request.POST.getlist(
        "administrative_increases_type"
    )
    administrative_increase_value = request.POST.getlist(
        "administrative_increase_value"
    )
    administrative_increases_for_every_year = request.POST.getlist(
        "administrative_increases_for_every_year"
    )
    administrative_count = len(administrative_increase_value)
    if administrative_count > 0:
        for i in range(0, administrative_count):
            if administrative_increase_value[i].strip() != "":
                administrative_increases_type_final += (
                    administrative_increases_type[i] + "-"
                )
                administrative_increase_value_final += (
                    administrative_increase_value[i] + "-"
                )
                administrative_increases_for_every_year_final += (
                    administrative_increases_for_every_year[i] + "-"
                )

    reim_increases_type_final = ""
    reim_increase_value_final = ""
    reim_increases_for_every_year_final = ""
    reim_increases_type = request.POST.getlist("reim_increases_type")
    reim_increase_value = request.POST.getlist("reim_increase_value")
    reim_increases_for_every_year = request.POST.getlist(
        "reim_increases_for_every_year"
    )
    reim_count = len(reim_increase_value)
    if reim_count > 0:
        for i in range(0, reim_count):
            if reim_increase_value[i].strip() != "":
                reim_increases_type_final += reim_increases_type[i] + "-"
                reim_increase_value_final += reim_increase_value[i] + "-"
                reim_increases_for_every_year_final += (
                    reim_increases_for_every_year[i] + "-"
                )

    if request.POST.get("report_id"):
        report_id = request.POST.get("report_id")
        report = Reports.objects.filter(id=int(report_id)).update(
            asset_name=request.POST.get("asset_name"),
            acquired_on=request.POST.get("acquired_on"),
            original_purchase_price=int(
                getNum(request.POST.get("original_purchase_price"))
            ),
            mortgage_loan=int(float(getNum(request.POST.get("mortgage_loan")))),
            no_years=request.POST.get("no_years"),
            amount_down_payment=int(
                float(getNum(request.POST.get("amount_down_payment")))
            ),
            ammortization_years=int(
                float(getNum(request.POST.get("ammortization_years")))
            ),
            annual_rate_interests=request.POST.get("annual_rate_interests"),
            avg_exp=int(float(getNum(request.POST.get("avg_exp")))),
            noi=int(float(getNum(request.POST.get("noi")))),
            cap_rate=int(float(getNum(request.POST.get("cap_rate")))),
            closing_expenses=0,
            expense_taxes=int(float(getNum(request.POST.get("expense_taxes")))),
            taxes_ye_mo=request.POST.get("taxes_ye_mo"),
            taxes_frequency=request.POST.get("taxes_frequency"),
            taxes_increases_type=taxes_increases_type_final,
            taxes_increase_value=taxes_increase_value_final,
            taxes_increases_for_every_year=taxes_increases_for_every_year_final,
            expense_hoa=int(float(getNum(request.POST.get("expense_hoa")))),
            hoa_ye_mo=request.POST.get("hoa_ye_mo"),
            hoa_frequency=request.POST.get("hoa_frequency"),
            hoa_increases_type=hoa_increases_type_final,
            hoa_increase_value=hoa_increase_value_final,
            hoa_increases_for_every_year=hoa_increases_for_every_year_final,
            gross_income=int(float(getNum(request.POST.get("gross_income")))),
            expense_vacancy=int(float(getNum(request.POST.get("expense_vacancy")))),
            expense_vacancy_type=request.POST.get("expense_vacancy_type"),
            debt_service_ratio=request.POST.get("debt_service_ratio"),
            amount_down_payment_value=int(
                getNum(request.POST.get("amount_down_payment_value"))
            ),
            amount_down_payment_type=request.POST.get("amount_down_payment_type"),
            total_sft=request.POST.get("total_sft"),
            no_units=request.POST.get("no_units"),
            asset_appraisal_type=request.POST.get("asset_appraisal_type"),
            asset_appraisal_value=int(
                float(getNum(request.POST.get("asset_appraisal_value")))
            ),
            sales_expense_type=request.POST.get("sales_expense_type"),
            sales_expense_value=int(
                float(getNum(request.POST.get("sales_expense_value")))
            ),
            insurance_expense=int(float(getNum(request.POST.get("insurance_expense")))),
            insu_ye_mo=request.POST.get("insu_ye_mo"),
            insu_frequency=request.POST.get("insu_frequency"),
            insu_increases_type=insu_increases_type_final,
            insu_increase_value=insu_increase_value_final,
            insu_increases_for_every_year=insu_increases_for_every_year_final,
            expense_cam=int(float(getNum(request.POST.get("expense_cam")))),
            cam_ye_mo=request.POST.get("cam_ye_mo"),
            cam_frequency=request.POST.get("cam_frequency"),
            cam_increases_type=cam_increases_type_final,
            cam_increase_value=cam_increase_value_final,
            cam_increases_for_every_year=cam_increases_for_every_year_final,
            reimbursement_income=int(
                float(getNum(request.POST.get("reimbursement_income")))
            ),
            reim_ye_mo=request.POST.get("reim_ye_mo"),
            reim_frequency=request.POST.get("reim_frequency"),
            reim_increases_type=reim_increases_type_final,
            reim_increase_value=reim_increase_value_final,
            reim_increases_for_every_year=reim_increases_for_every_year_final,
            expense_utilities=int(float(getNum(request.POST.get("expense_utilities")))),
            utilities_ye_mo=request.POST.get("utilities_ye_mo"),
            utilities_frequency=request.POST.get("utilities_frequency"),
            utilities_increases_type=utilities_increases_type_final,
            utilities_increase_value=utilities_increase_value_final,
            utilities_increases_for_every_year=utilities_increases_for_every_year_final,
            expense_management=int(
                float(getNum(request.POST.get("expense_management")))
            ),
            management_ye_mo=request.POST.get("management_ye_mo"),
            management_frequency=request.POST.get("management_frequency"),
            management_increases_type=management_increases_type_final,
            management_increase_value=management_increase_value_final,
            management_increases_for_every_year=management_increases_for_every_year_final,
            expense_administrative=int(
                float(getNum(request.POST.get("expense_administrative")))
            ),
            administrative_ye_mo=request.POST.get("administrative_ye_mo"),
            administrative_frequency=request.POST.get("administrative_frequency"),
            administrative_increases_type=administrative_increases_type_final,
            administrative_increase_value=administrative_increase_value_final,
            administrative_increases_for_every_year=administrative_increases_for_every_year_final,
            year1_roi=request.POST.get("year1_roi"),
            total_roi_percentage=request.POST.get("total_roi_percentage"),
            total_roi=request.POST.get("total_roi"),
            cloned=0,
            updated_at=datetime.now(),
        )
        if request.POST.get("tenant_id"):
            tenant_ids = request.POST.getlist("tenant_id")
            for i, tenant_id in enumerate(tenant_ids):
                tenant_name_edit = request.POST.getlist("tenant_name_edit")
                lease_rate_edit = request.POST.getlist("lease_rate_edit")
                sft_leased_edit = request.POST.getlist("sft_leased_edit")
                rent_frequency_edit = request.POST.getlist("rent_frequency_edit")
                lease_rate_type_edit = request.POST.getlist("lease_rate_type_edit")
                rent_increases_edit = request.POST.getlist(
                    "rent_increases_edit[" + str(i) + "]"
                )
                rent_increase_value_edit = request.POST.getlist(
                    "rent_increase_value_edit[" + str(i) + "]"
                )
                rent_increases_for_every_year_edit = request.POST.getlist(
                    "rent_increases_for_every_year_edit[" + str(i) + "]"
                )
                rent_increases_final = ""
                rent_increase_value_final = ""
                rent_increases_for_every_year_final = ""

                for j in range(0, len(rent_increases_edit)):
                    rent_increases_final += rent_increases_edit[j] + "-"
                    rent_increase_value_final += rent_increase_value_edit[j] + "-"
                    rent_increases_for_every_year_final += (
                        rent_increases_for_every_year_edit[j] + "-"
                    )
                affected = Tenants.objects.filter(id=tenant_id).update(
                    tenant_name=tenant_name_edit[i],
                    lease_rate=lease_rate_edit[i],
                    lease_rate_type=lease_rate_type_edit[i],
                    rent_frequency=rent_frequency_edit[i],
                    sft_leased=sft_leased_edit[i],
                    rent_increases=rent_increases_final,
                    rent_increase_value=rent_increase_value_final,
                    rent_increases_for_every_year=rent_increases_for_every_year_final,
                )

        if request.POST.get("tenant_name"):
            tenant_name = request.POST.getlist("tenant_name")
            lease_rate = request.POST.getlist("lease_rate")
            sft_leased = request.POST.getlist("sft_leased")
            rent_frequency = request.POST.getlist("rent_frequency")
            lease_rate_type = request.POST.getlist("lease_rate_type")
            tenant_nums = request.POST.get("tenant_nums").split(",")
            tenant_count = len(tenant_name)
            if tenant_count > 0:
                for i in range(0, tenant_count):
                    rent_increases = removeempty(
                        request.POST.getlist(
                            "rent_increases[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increase_value = removeempty(
                        request.POST.getlist(
                            "rent_increase_value[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "rent_increases_for_every_year[" + str(tenant_nums[i]) + "]"
                        )
                    )
                    rent_increases_final = ""
                    rent_increase_value_final = ""
                    rent_increases_for_every_year_final = ""
                    if tenant_name[i].strip() != "":
                        for j in range(0, len(rent_increases)):
                            rent_increases_final += rent_increases[j] + "-"
                            rent_increase_value_final += rent_increase_value[j] + "-"
                            rent_increases_for_every_year_final += (
                                rent_increases_for_every_year[j] + "-"
                            )
                        tenant = Tenants.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            tenant_name=tenant_name[i],
                            lease_rate=lease_rate[i],
                            lease_rate_type=lease_rate_type[i],
                            rent_frequency=rent_frequency[i],
                            sft_leased=sft_leased[i],
                            rent_increases=rent_increases_final,
                            rent_increase_value=rent_increase_value_final,
                            rent_increases_for_every_year=rent_increases_for_every_year_final,
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        if request.POST.get("additional_expense_id").strip():
            expense_head_ids = request.POST.getlist("additional_expense_id")
            # print("expense_head_ids", expense_head_ids)
            for i, additional_expense_id in enumerate(expense_head_ids):
                expense_head_name_edit = request.POST.getlist("expense_head_name_edit")
                expense_amount_edit = request.POST.getlist("expense_amount_edit")
                expense_frequency_edit = request.POST.getlist("expense_frequency_edit")
                expense_increases_type_edit = request.POST.getlist(
                    "expense_increases_type_edit[" + str(i) + "]"
                )
                expense_increase_value_edit = request.POST.getlist(
                    "expense_increase_value_edit[" + str(i) + "]"
                )
                expense_increases_for_every_year_edit = request.POST.getlist(
                    "expense_increases_for_every_year_edit[" + str(i) + "]"
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                for j in range(0, len(expense_increases_type_edit)):
                    expense_increases_final += expense_increases_type_edit[j] + "-"
                    expense_increase_value_final += expense_increase_value_edit[j] + "-"
                    expense_increases_for_every_year_final += (
                        expense_increases_for_every_year_edit[j] + "-"
                    )

                affected = Subheads.objects.filter(
                    id=int(additional_expense_id)
                ).update(
                    report_id=int(request.POST.get("report_id")),
                    title=expense_head_name_edit[i],
                    amount=int(float(getNum(expense_amount_edit[i]))),
                    increases_type=expense_increases_final,
                    increase_value=expense_increase_value_final,
                    frequency=expense_frequency_edit[i],
                    increases_for_every_year=expense_increases_for_every_year_final,
                    type="expense",
                )

        if request.POST.get("expense_head_name"):
            expense_head_name = request.POST.getlist("expense_head_name")
            expense_amount = request.POST.getlist("expense_amount")
            frequency = request.POST.getlist("expense_frequency")
            additional_expenses_nums = request.POST.get(
                "additional_expenses_nums"
            ).split(",")
            expense_head_count = len(expense_head_name)
            if expense_head_count > 0:
                for i in range(0, expense_head_count):
                    increases_type = removeempty(
                        request.POST.getlist(
                            "expense_increases_type["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    increase_value = removeempty(
                        request.POST.getlist(
                            "expense_increase_value["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "expense_increases_for_every_year["
                            + str(additional_expenses_nums[i])
                            + "]"
                        )
                    )
                    expense_increases_final = ""
                    expense_increase_value_final = ""
                    expense_increases_for_every_year_final = ""
                    for j in range(len(increases_type)):
                        expense_increases_final += increases_type[j] + "-"
                        expense_increase_value_final += increase_value[j] + "-"
                        expense_increases_for_every_year_final += (
                            increases_for_every_year[j] + "-"
                        )
                    if expense_head_name[i].strip() != "":
                        subhead = Subheads.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            title=expense_head_name[i],
                            amount=int(float(getNum(expense_amount[i]))),
                            increases_type=expense_increases_final,
                            increase_value=expense_increase_value_final,
                            frequency=frequency[i],
                            increases_for_every_year=expense_increases_for_every_year_final,
                            type="expense",
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        if request.POST.get("additional_income_id"):
            additional_income_ids = request.POST.getlist("additional_income_id")
            for i, additional_income_id in enumerate(additional_income_ids):
                expense_head_name_edit = request.POST.getlist("expense_head_name_edit")
                expense_amount_edit = request.POST.getlist("expense_amount_edit")
                expense_frequency_edit = request.POST.getlist("expense_frequency_edit")
                expense_increases_type_edit = request.POST.getlist(
                    "expense_increases_type_edit[" + str(i) + "]"
                )
                expense_increase_value_edit = request.POST.getlist(
                    "expense_increase_value_edit[" + str(i) + "]"
                )
                expense_increases_for_every_year_edit = request.POST.getlist(
                    "expense_increases_for_every_year_edit[" + str(i) + "]"
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                income_name_edit = request.POST.getlist("income_name_edit")
                income_amount_edit = request.POST.getlist("income_amount_edit")
                income_frequency_edit = request.POST.getlist("income_frequency_edit")
                income_increases_type_edit = request.POST.getlist(
                    "income_increases_type_edit[" + str(i) + "]"
                )
                income_increase_value_edit = request.POST.getlist(
                    "income_increase_value_edit[" + str(i) + "]"
                )
                income_increases_for_every_year_edit = request.POST.getlist(
                    "income_increases_for_every_year_edit[" + str(i) + "]"
                )
                income_increases_final = ""
                income_increase_value_final = ""
                income_increases_for_every_year_final = ""
                for j in range(0, len(income_increases_type_edit)):
                    income_increases_final += income_increases_type_edit[j] + "-"
                    income_increase_value_final += income_increase_value_edit[j] + "-"
                    income_increases_for_every_year_final += (
                        income_increases_for_every_year_edit[j] + "-"
                    )

                affected = Subheads.objects.filter(id=additional_income_id).update(
                    report_id=int(request.POST.get("report_id")),
                    title=income_name_edit[i],
                    amount=int(float(getNum(income_amount_edit[i]))),
                    increases_type=income_increases_final,
                    increase_value=income_increase_value_final,
                    frequency=income_frequency_edit[i],
                    increases_for_every_year=income_increases_for_every_year_final,
                    type="income",
                )

        if request.POST.get("income_name"):
            income_name = request.POST.getlist("income_name")
            income_amount = request.POST.getlist("income_amount")
            frequency = request.POST.getlist("income_frequency")
            additional_income_nums = request.POST.get("additional_income_nums").split(
                ","
            )
            income_name_count = len(income_name)
            if income_name_count > 0:
                for i in range(0, income_name_count):
                    increases_type = removeempty(
                        request.POST.getlist(
                            "income_increases_type["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    increase_value = removeempty(
                        request.POST.getlist(
                            "income_increase_value["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    increases_for_every_year = removeempty(
                        request.POST.getlist(
                            "income_increases_for_every_year["
                            + str(additional_income_nums[i])
                            + "]"
                        )
                    )
                    income_increases_final = ""
                    income_increase_value_final = ""
                    income_increases_for_every_year_final = ""
                    for j in range(0, len(increases_type)):
                        income_increases_final += increases_type[j] + "-"
                        income_increase_value_final += increase_value[j] + "-"
                        income_increases_for_every_year_final += (
                            increases_for_every_year[j] + "-"
                        )

                    if income_name[i].strip() != "":
                        subhead = Subheads.objects.create(
                            user_id=user.id,
                            report_id=report_id,
                            title=income_name[i],
                            amount=int(float(getNum(income_amount[i]))),
                            increases_type=income_increases_final,
                            increase_value=income_increase_value_final,
                            frequency=frequency[i],
                            increases_for_every_year=income_increases_for_every_year_final,
                            type="income",
                            created_at=datetime.now(),
                            updated_at=datetime.now(),
                        )

        closing_expensename = request.POST.get("closing_expensename")
        closing_expenseamount = request.POST.get("closing_expenseamount")
        affected = Subheads.objects.filter(
            report_id=request.POST.get("report_id"), type="closing_expense"
        ).update(
            title=closing_expensename, amount=int(float(getNum(closing_expenseamount)))
        )

        closing_consession_name = request.POST.get("closing_consession_name")
        closing_consessionamount = request.POST.get("closing_consessionamount")
        affected = Subheads.objects.filter(
            report_id=request.POST.get("report_id"), type="closing_consession"
        ).update(
            title=closing_consession_name,
            amount=int(float(getNum(closing_consessionamount))),
        )
        url = "%s?id=%s" % (
            reverse("userapp:comm-roi"),
            str(request.POST.get("report_id")).strip(),
        )
        return redirect(url)

    else:
        report = Reports.objects.create(
            user_id=user.id,
            asset_name=request.POST.get("asset_name"),
            analysis_type=request.POST.get("analysis_type"),
            acquired_on=request.POST.get("acquired_on"),
            original_purchase_price=int(
                getNum(request.POST.get("original_purchase_price"))
            ),
            closing_concession=0,
            mortgage_loan=int(float(getNum(request.POST.get("mortgage_loan")))),
            no_years=request.POST.get("no_years"),
            amount_down_payment=int(
                float(getNum(request.POST.get("amount_down_payment")))
            ),
            ammortization_years=int(
                float(getNum(request.POST.get("ammortization_years")))
            ),
            annual_rate_interests=request.POST.get("annual_rate_interests"),
            avg_exp=int(float(getNum(request.POST.get("avg_exp")))),
            noi=int(float(getNum(request.POST.get("noi")))),
            cap_rate=int(float(getNum(request.POST.get("cap_rate")))),
            closing_expenses=0,
            expense_taxes=int(float(getNum(request.POST.get("expense_taxes")))),
            taxes_ye_mo=request.POST.get("taxes_ye_mo"),
            taxes_frequency=request.POST.get("taxes_frequency"),
            taxes_increases_type=taxes_increases_type_final,
            taxes_increase_value=taxes_increase_value_final,
            taxes_increases_for_every_year=taxes_increases_for_every_year_final,
            expense_hoa=int(float(getNum(request.POST.get("expense_hoa")))),
            hoa_ye_mo=request.POST.get("hoa_ye_mo"),
            hoa_frequency=request.POST.get("hoa_frequency"),
            hoa_increases_type=hoa_increases_type_final,
            hoa_increase_value=hoa_increase_value_final,
            hoa_increases_for_every_year=hoa_increases_for_every_year_final,
            gross_income=int(float(getNum(request.POST.get("gross_income")))),
            expense_vacancy=int(float(getNum(request.POST.get("expense_vacancy")))),
            expense_vacancy_type=request.POST.get("expense_vacancy_type"),
            debt_service_ratio=request.POST.get("debt_service_ratio"),
            amount_down_payment_value=int(
                getNum(request.POST.get("amount_down_payment_value"))
            ),
            amount_down_payment_type=request.POST.get("amount_down_payment_type"),
            total_sft=request.POST.get("total_sft"),
            no_units=request.POST.get("no_units"),
            asset_appraisal_type=request.POST.get("asset_appraisal_type"),
            asset_appraisal_value=int(
                float(getNum(request.POST.get("asset_appraisal_value")))
            ),
            sales_expense_type=request.POST.get("sales_expense_type"),
            sales_expense_value=int(
                float(getNum(request.POST.get("sales_expense_value")))
            ),
            insurance_expense=int(float(getNum(request.POST.get("insurance_expense")))),
            insu_ye_mo=request.POST.get("insu_ye_mo"),
            insu_frequency=request.POST.get("insu_frequency"),
            insu_increases_type=insu_increases_type_final,
            insu_increase_value=insu_increase_value_final,
            insu_increases_for_every_year=insu_increases_for_every_year_final,
            expense_cam=int(float(getNum(request.POST.get("expense_cam")))),
            cam_ye_mo=request.POST.get("cam_ye_mo"),
            cam_frequency=request.POST.get("cam_frequency"),
            cam_increases_type=cam_increases_type_final,
            cam_increase_value=cam_increase_value_final,
            cam_increases_for_every_year=cam_increases_for_every_year_final,
            reimbursement_income=int(
                float(getNum(request.POST.get("reimbursement_income")))
            ),
            reim_ye_mo=request.POST.get("reim_ye_mo"),
            reim_frequency=request.POST.get("reim_frequency"),
            reim_increases_type=reim_increases_type_final,
            reim_increase_value=reim_increase_value_final,
            reim_increases_for_every_year=reim_increases_for_every_year_final,
            expense_utilities=int(float(getNum(request.POST.get("expense_utilities")))),
            utilities_ye_mo=request.POST.get("utilities_ye_mo"),
            utilities_frequency=request.POST.get("utilities_frequency"),
            utilities_increases_type=utilities_increases_type_final,
            utilities_increase_value=utilities_increase_value_final,
            utilities_increases_for_every_year=utilities_increases_for_every_year_final,
            expense_management=int(
                float(getNum(request.POST.get("expense_management")))
            ),
            management_ye_mo=request.POST.get("management_ye_mo"),
            management_frequency=request.POST.get("management_frequency"),
            management_increases_type=management_increases_type_final,
            management_increase_value=management_increase_value_final,
            management_increases_for_every_year=management_increases_for_every_year_final,
            expense_administrative=int(
                float(getNum(request.POST.get("expense_administrative")))
            ),
            administrative_ye_mo=request.POST.get("administrative_ye_mo"),
            administrative_frequency=request.POST.get("administrative_frequency"),
            administrative_increases_type=administrative_increases_type_final,
            administrative_increase_value=administrative_increase_value_final,
            administrative_increases_for_every_year=administrative_increases_for_every_year_final,
            year1_roi=request.POST.get("year1_roi"),
            total_roi_percentage=request.POST.get("total_roi_percentage"),
            total_roi=request.POST.get("total_roi"),
            cloned=0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        tenant_name = request.POST.getlist("tenant_name")
        lease_rate = request.POST.getlist("lease_rate")
        sft_leased = request.POST.getlist("sft_leased")
        rent_frequency = request.POST.getlist("rent_frequency")
        lease_rate_type = request.POST.getlist("lease_rate_type")
        tenant_nums = request.POST.get("tenant_nums").split(",")
        tenant_count = len(tenant_name)
        if tenant_count > 0:
            for i in range(0, tenant_count):
                rent_increases = removeempty(
                    request.POST.getlist("rent_increases[" + str(tenant_nums[i]) + "]")
                )
                rent_increase_value = removeempty(
                    request.POST.getlist(
                        "rent_increase_value[" + str(tenant_nums[i]) + "]"
                    )
                )
                rent_increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "rent_increases_for_every_year[" + str(tenant_nums[i]) + "]"
                    )
                )
                rent_increases_final = ""
                rent_increase_value_final = ""
                rent_increases_for_every_year_final = ""
                if tenant_name[i].strip() != "":
                    for j in range(0, len(rent_increases)):
                        rent_increases_final += rent_increases[j] + "-"
                        rent_increase_value_final += rent_increase_value[j] + "-"
                        rent_increases_for_every_year_final += (
                            rent_increases_for_every_year[j] + "-"
                        )
                    tenant = Tenants.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        tenant_name=tenant_name[i],
                        lease_rate=lease_rate[i],
                        lease_rate_type=lease_rate_type[i],
                        rent_frequency=rent_frequency[i],
                        sft_leased=sft_leased[i],
                        rent_increases=rent_increases_final,
                        rent_increase_value=rent_increase_value_final,
                        rent_increases_for_every_year=rent_increases_for_every_year_final,
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        expense_head_name = request.POST.getlist("expense_head_name")
        expense_amount = request.POST.getlist("expense_amount")
        frequency = request.POST.getlist("expense_frequency")
        additional_expenses_nums = request.POST.get("additional_expenses_nums").split(
            ","
        )
        expense_head_count = len(expense_head_name)
        if expense_head_count > 0:
            for i in range(0, expense_head_count):
                increases_type = removeempty(
                    request.POST.getlist(
                        "expense_increases_type["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                increase_value = removeempty(
                    request.POST.getlist(
                        "expense_increase_value["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "expense_increases_for_every_year["
                        + str(additional_expenses_nums[i])
                        + "]"
                    )
                )
                expense_increases_final = ""
                expense_increase_value_final = ""
                expense_increases_for_every_year_final = ""
                for j in range(len(increases_type)):
                    expense_increases_final += increases_type[j] + "-"
                    expense_increase_value_final += increase_value[j] + "-"
                    expense_increases_for_every_year_final += (
                        increases_for_every_year[j] + "-"
                    )
                if expense_head_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=expense_head_name[i],
                        amount=int(float(getNum(expense_amount[i]))),
                        increases_type=expense_increases_final,
                        increase_value=expense_increase_value_final,
                        frequency=frequency[i],
                        increases_for_every_year=expense_increases_for_every_year_final,
                        type="expense",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        income_name = request.POST.getlist("income_name")
        income_amount = request.POST.getlist("income_amount")
        frequency = request.POST.getlist("income_frequency")
        additional_income_nums = request.POST.get("additional_income_nums").split(",")
        income_name_count = len(income_name)
        if income_name_count > 0:
            for i in range(0, income_name_count):
                increases_type = removeempty(
                    request.POST.getlist(
                        "income_increases_type[" + str(additional_income_nums[i]) + "]"
                    )
                )
                increase_value = removeempty(
                    request.POST.getlist(
                        "income_increase_value[" + str(additional_income_nums[i]) + "]"
                    )
                )
                increases_for_every_year = removeempty(
                    request.POST.getlist(
                        "income_increases_for_every_year["
                        + str(additional_income_nums[i])
                        + "]"
                    )
                )
                income_increases_final = ""
                income_increase_value_final = ""
                income_increases_for_every_year_final = ""
                for j in range(0, len(increases_type)):
                    income_increases_final += increases_type[j] + "-"
                    income_increase_value_final += increase_value[j] + "-"
                    income_increases_for_every_year_final += (
                        increases_for_every_year[j] + "-"
                    )

                if income_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=income_name[i],
                        amount=int(float(getNum(income_amount[i]))),
                        increases_type=income_increases_final,
                        increase_value=income_increase_value_final,
                        frequency=frequency[i],
                        increases_for_every_year=income_increases_for_every_year_final,
                        type="income",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        closing_expensename = request.POST.getlist("closing_expensename")
        closing_expenseamount = request.POST.getlist("closing_expenseamount")
        closing_expensename_count = len(closing_expensename)
        if closing_expensename_count > 0:
            for i in range(0, closing_expensename_count):
                if closing_expensename[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=closing_expensename[i],
                        amount=int(float(getNum(closing_expenseamount[i]))),
                        type="closing_expense",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )

        closing_consession_name = request.POST.getlist("closing_consession_name")
        closing_consessionamount = request.POST.getlist("closing_consessionamount")
        closing_consession_name_count = len(closing_consession_name)
        if closing_consession_name_count > 0:
            for i in range(0, closing_consession_name_count):
                if closing_consession_name[i].strip() != "":
                    subhead = Subheads.objects.create(
                        user_id=user.id,
                        report_id=report.id,
                        title=closing_consession_name[i],
                        amount=int(float(getNum(closing_consessionamount[i]))),
                        type="closing_consession",
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )
        url = "%s?id=%s" % (reverse("userapp:comm-roi"), str(report.id))
        return redirect(url)
        return HttpResponse("<h1>Saved Commercial Roi Reports</h1>")


def delete_tenant(request, id):
    Tenants.objects.get(id=int(id)).delete()
    return JsonResponse({"success": "'Tenant deleted successfully!'"})


def delete_tenant_escalations(request, id):
    t_id = id.split("-")
    tenant = Tenants.objects.filter(id=int(t_id[0])).first()
    pos = t_id[1]
    rent_increases_str = tenant.rent_increases.split("-")
    del rent_increases_str[int(pos)]
    rent_increases = "-".join(rent_increases_str)

    rent_increase_value_str = tenant.rent_increase_value.split("-")
    del rent_increase_value_str[int(pos)]
    rent_increase_value = "-".join(rent_increase_value_str)

    rent_increases_for_every_year_str = tenant.rent_increase_value.split("-")
    del rent_increases_for_every_year_str[int(pos)]
    rent_increases_for_every_year = "-".join(rent_increases_for_every_year_str)

    Tenants.objects.filter(id=int(t_id[0])).update(
        rent_increases=rent_increases,
        rent_increase_value=rent_increase_value,
        rent_increases_for_every_year=rent_increases_for_every_year,
    )

    return JsonResponse({"success": "Tenant Escalations deleted successfully!"})


def delete_additional_escalations(request, id):
    a_id = id.split("-")
    subhead = Subheads.objects.filter(id=int(a_id[0])).first()
    pos = a_id[1]
    increases_type_str = subhead.increases_type.split("-")
    del increases_type_str[int(pos)]
    increases_type = "-".join(increases_type_str)

    increase_value_str = subhead.increase_value.split("-")
    del increase_value_str[int(pos)]
    increase_value = "-".join(increase_value_str)

    increases_for_every_year_str = subhead.increases_for_every_year.split("-")
    del increases_for_every_year_str[int(pos)]
    increases_for_every_year = "-".join(increases_for_every_year_str)

    Subheads.objects.filter(id=int(a_id[0])).update(
        increases_type=increases_type,
        increase_value=increase_value,
        increases_for_every_year=increases_for_every_year,
    )
    return JsonResponse({"success": "Escalations deleted successfully!"})


def delete_subheads(request, id):
    Subheads.objects.filter(id=int(id)).delete()
    return JsonResponse({"success": "deleted successfully!"})
