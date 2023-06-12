import math
from userapp.models import *
from datetime import datetime


def amort(
    request,
    lease_rate_type,
    amount_down_payment,
    insurance_expense,
    insu_ye_mo,
    insu_frequency,
    insu_increases_type,
    insu_increase_value,
    insu_increases_for_every_year,
    mortagage_loan,
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
    expense_maintenance_set,
    expense_vacancy_set,
    property_mgmt_set,
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
    mortagage_interest,
    calcTerms_initial,
):
    amort_dynamic_input_update = {}
    # Calculate the per month interest rate
    monthlyRate = interestRate / 12
    if lease_rate_type == 0:
        year_lease = lease_rate * sft_leased
        year_lease2 = lease_rate * sft_leased
        year_lease3 = lease_rate * sft_leased
        year_lease4 = lease_rate * sft_leased
        year_leasex = lease_rate * sft_leased
        year_leasez = lease_rate * sft_leased
        year_leasezy = lease_rate * sft_leased
        year_leasey = lease_rate * sft_leased
        year_lease25 = lease_rate * sft_leased
        year_leasezz = lease_rate * sft_leased
        year_leasemm = lease_rate * sft_leased
        year_leasekk = lease_rate * sft_leased
        year_leaseyy = lease_rate * sft_leased
        year_leasenn = lease_rate * sft_leased
        year_leasezpy = lease_rate * sft_leased
        year_lease1 = lease_rate * sft_leased
        year_lease26 = lease_rate * sft_leased
    else:
        year_lease1 = lease_rate * 12
        year_lease = lease_rate * 12
        year_lease2 = lease_rate * 12
        year_lease3 = lease_rate * 12
        year_lease4 = lease_rate * 12
        year_lease1 = lease_rate * 12
        year_leasex = lease_rate * 12
        year_leasez = lease_rate * 12
        year_leasezy = lease_rate * 12
        year_leasey = lease_rate * 12
        year_lease25 = lease_rate * 12
        year_leasezz = lease_rate * 12
        year_leasemm = lease_rate * 12
        year_leasekk = lease_rate * 12
        year_leaseyy = lease_rate * 12
        year_leasenn = lease_rate * 12
        year_leasezpy = lease_rate * 12
        year_lease26 = lease_rate * 12

    mortagage_loan5 = mortagage_loan
    expense_taxes4 = expense_taxes
    expense_taxes1 = expense_taxes
    expense_taxes2 = expense_taxes
    expense_taxes3 = expense_taxes
    expense_taxes9 = expense_taxes
    expense_taxes10 = expense_taxes

    # Calculate the payment
    expense_insurance = insurance_expense
    expense_insurance1 = expense_insurance
    expense_insurance2 = expense_insurance
    expense_insurance3 = expense_insurance
    expense_insurance4 = expense_insurance
    expense_insurance9 = expense_insurance
    expense_insurance10 = expense_insurance
    result = ""
    result += "<table border='1' class='table table-sm'   width='1000px' id='investment_analysis' ><thead> <tr>  "
    result += "<th>Tenant Name</th>"
    for count in range(0, terms):
        result += "<th id='Year'>Year " + str(count + 1) + " Lease</th>"

    tenant_list = request.POST.getlist("tenant_name")

    sft_leased_list = request.POST.getlist("sft_leased")

    lease_rate_type_list = request.POST.getlist("lease_rate_type")

    lease_rate_list = request.POST.getlist("lease_rate")

    rent_frequency_list = request.POST.getlist("rent_frequency")

    rent_increases_list = request.POST.getlist("rent_increases")
    rent_increase_value_list = request.POST.getlist("rent_increase_value")
    rent_increases_for_every_year_list = request.POST.getlist(
        "rent_increases_for_every_year"
    )

    SumofAmountYearWise = []

    for i in range(0, len(tenant_list)):
        if lease_rate_type == 0:
            year_lease1 = sft_leased_list[i] * lease_rate_list[i]
        else:
            year_lease1 = lease_rate_list[i] * 12
        result += " </tr></thead><tbody> <tr><td>" + tenant_list[i] + "</td>"
        lease_rate = lease_rate_list[i]
        for count in range(0, terms):
            if int(rent_frequency_list[i]) == 1:
                count2 = count + 1
            else:
                count2 = count
            tenant_count = i
            lease_rate = year_lease_calc2(
                request,
                lease_rate,
                count2,
                tenant_count,
            )
            if not lease_rate:
                lease_rate = 0
            if int(lease_rate_type_list[i]) == 1:
                year_lease2 = lease_rate * 12
            else:
                if sft_leased_list[i]:
                    year_lease2 = float(lease_rate) * float(sft_leased_list[i])
                else:
                    year_lease2 = float(lease_rate) * 0
            if i == 0:
                SumofAmountYearWise.append(year_lease2)  # 10
            else:
                SumofAmountYearWise[count] = SumofAmountYearWise[count] + year_lease2
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"
            result += (
                "<td id=" + blurcss + "> $ " + str(round(year_lease2, 0)) + "</td>"
            )

    ####Additional Incomes#####
    additional_income_nums = request.POST.get("additional_income_nums").split(",")
    income_name_list = request.POST.getlist("income_name")
    income_amount_list = request.POST.getlist("income_amount")
    income_frequency_list = request.POST.getlist("income_frequency")
    SumofAllIncome = []
    for i in range(0, len(income_name_list)):
        income_increases_type_list = request.POST.getlist(
            "income_increases_type[" + str(additional_income_nums[i]) + "]"
        )
        income_increase_value_list = request.POST.getlist(
            "income_increase_value[" + str(additional_income_nums[i]) + "]"
        )
        income_increases_for_every_year_list = request.POST.getlist(
            "income_increases_for_every_year[" + str(additional_income_nums[i]) + "]"
        )

        result += (
            " </tr></thead><tbody> <tr><td>Additional Incomes - "
            + str(income_name_list[i])
            + "</td>"
        )
        for count in range(0, terms):
            if count == 0:
                if income_amount_list[i]:
                    income_amount = income_amount_list[i]
                else:
                    income_amount = 0
            additional_income_count = i
            income_amount = additional_income_calc(
                request,
                int(income_amount),
                int(income_frequency_list[i]),
                int(income_increases_type_list[0]),
                int(income_increase_value_list[0]),
                int(income_increases_for_every_year_list[0]),
                count,
                additional_income_count,
            )
            if i == 0:
                SumofAllIncome.append(income_amount)
            else:
                SumofAllIncome[count] = SumofAllIncome[count] + income_amount
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"
            result += (
                "<td id="
                + blurcss
                + "> $ "
                + str(round(float(income_amount), 0))
                + "</td>"
            )

    result += "</tr><tr><td>Closing Concession</td>"
    for count in range(0, terms):
        if count == 0:
            clos_conc = closing_concession
        else:
            clos_conc = 0
        result += "<td id=" + blurcss + "> $ " + str(clos_conc) + " </td>"

    result += "</tr><tr><td>Income - Yearly Total Rents</td>"

    for count in range(0, terms):
        if count == 0:
            clos_conc = closing_concession
        else:
            clos_conc = 0

        if (
            SumofAllIncome[count] == "undefined"
        ):  # check this what condition to keep , list out of index error handle i think
            SumofAllIncome[count] = 0
        all_income_slab = (
            float(SumofAmountYearWise[count])
            + float(clos_conc)
            + float(SumofAllIncome[count])
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(round(all_income_slab)) + "</td>"

    result += "</tr><tr><td>Expenses - Taxes</td>"
    for count in range(0, terms):
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        expense_taxes = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        result += "<td id=" + blurcss + "> $ " + str(round(expense_taxes, 0)) + "</td>"

    result += "</tr><tr><td>Expenses - Insurance</td>"
    for count in range(0, terms):
        expense_insurance = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + "> $ " + str(round(expense_insurance, 0)) + "</td>"
        )

    result += "</tr><tr><td>Expenses - HOA</td>"
    for count in range(0, terms):
        expense_hoa1 = expense_hoa
        expense_hoa1 = hoa_calc(
            request,
            expense_hoa1,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(round(expense_hoa1, 0)) + "</td>"

    if expense_maintenance_type == 0:
        expense_maintenance_type_disp = "%"
    else:
        expense_maintenance_type_disp = "$"
    result += (
        "</tr><tr><td>Expense - Maintenance @ "
        + str(expense_maintenance_set)
        + " "
        + expense_maintenance_type_disp
        + "</td>"
    )
    for count in range(0, terms):
        year_lease26 = SumofAmountYearWise[count]
        year_lease_exp = expense_maintenance_calc(
            year_lease26, expense_maintenance_set, expense_maintenance_type
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(float(year_lease_exp), 0))
            + "</td>"
        )

    if expense_vacancy_type == 0:
        expense_vacancy_type_disp = "%"
    else:
        expense_vacancy_type_disp = "$"
    result += (
        "</tr><tr><td>Expenses - Vacancy @"
        + str(expense_vacancy_set)
        + " "
        + expense_vacancy_type_disp
        + "</td>"
    )
    for count in range(0, terms):
        year_lease3 = SumofAmountYearWise[count]
        expense_vacancy = expense_vacancy_calc(
            year_lease3, expense_vacancy_set, expense_vacancy_type
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(float(expense_vacancy), 0))
            + "</td>"
        )

    if property_mgmt_type == 0:
        property_mgmt_type_disp = "%"
    else:
        property_mgmt_type_disp = "$"

    result += (
        "</tr><tr><td>Expenses - Property Management @"
        + str(property_mgmt_set)
        + " "
        + property_mgmt_type_disp
        + "</td>"
    )
    for count in range(0, terms):
        year_lease4 = SumofAmountYearWise[count]
        expense_property = property_mgmt_calc(
            year_lease4, property_mgmt_set, property_mgmt_type
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(float(expense_property), 0))
            + "</td>"
        )

    ###Additional Expenses####
    expense_head_name_list = request.POST.getlist("expense_head_name")
    expense_amount_list = request.POST.getlist("expense_amount")
    expense_frequency_list = request.POST.getlist("expense_frequency")
    additional_expenses_nums = request.POST.get("additional_expenses_nums").split(",")
    SumofAllExpense = []
    for i in range(0, len(expense_head_name_list)):
        expense_increases_type_list = request.POST.getlist(
            "expense_increases_type[" + str(additional_expenses_nums[i]) + "]"
        )
        expense_increase_value_list = request.POST.getlist(
            "expense_increase_value[" + str(additional_expenses_nums[i]) + "]"
        )
        expense_increases_for_every_year_list = request.POST.getlist(
            "expense_increases_for_every_year[" + str(additional_expenses_nums[i]) + "]"
        )

        result += (
            " </tr></thead><tbody> <tr><td>Additional Expenses - "
            + str(expense_head_name_list[i])
            + "</td>"
        )
        for count in range(0, terms):
            if count == 0:
                if expense_amount_list[i]:
                    expense_amount = float(expense_amount_list[i])
                else:
                    expense_amount = 0
            additional_expenses_count = i
            expense_amount = additional_expense_calc(
                request,
                expense_amount,
                int(expense_frequency_list[i]),
                int(expense_increases_type_list[0]),
                int(expense_increase_value_list[0]),
                int(expense_increases_for_every_year_list[0]),
                count,
                additional_expenses_count,
            )
            if i == 0:
                SumofAllExpense.append(expense_amount)  # 10
            else:
                SumofAllExpense[count] = SumofAllExpense[count] + expense_amount
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"

            result += (
                "<td id="
                + blurcss
                + "> $ "
                + str(round(float(expense_amount)))
                + "</td>"
            )

    result += "</tr><tr><td>Closing Expenses</td>"
    for count in range(0, terms):
        if count == 0:
            clos_exp = closing_expenses
        else:
            clos_exp = 0

        result += "<td id=" + blurcss + "> $ " + str(clos_exp) + " </td>"

    result += "</tr><tr><td>Total Expenses</td>"
    for count in range(0, terms):
        year_leasez = SumofAmountYearWise[count]
        yearly_expense_vacancy = expense_vacancy_calc(
            year_leasez, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt = property_mgmt_calc(
            year_leasez, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance = expense_maintenance_calc(
            year_leasez, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes1 = expense_taxes_calc(
            request,
            expense_taxes1,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance1 = expense_insurance_calc(
            request,
            expense_insurance1,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(yearly_expense_vacancy)
            + float(yearly_property_mgmt)
            + float(yearly_expense_maintenance)
            + float(expense_taxes1)
            + float(yearly_expense_hoa)
            + float(expense_insurance1)
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if SumofAllExpense[count] == "undefined":  # check this condition
            SumofAllExpense[count] = 0
        total_year_calc_new_in = SumofAllIncome[count] + SumofAmountYearWise[count]
        total_year_calc_new_exp = total_year_calc + SumofAllExpense[count]
        total_year_calc_new = total_year_calc_new_in - total_year_calc_new_exp
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + "> $ " + str(round(total_year_calc_new_exp)) + "</td>"
        )

    result += "</tr><tr><td>NOI (Yearly Total - Expenses)</td>"
    for count in range(0, terms):
        year_leasez = SumofAmountYearWise[count]
        yearly_expense_vacancy = expense_vacancy_calc(
            year_leasez, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt = property_mgmt_calc(
            year_leasez, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance = expense_maintenance_calc(
            year_leasez, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes10 = expense_taxes_calc(
            request,
            expense_taxes10,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance10 = expense_insurance_calc(
            request,
            expense_insurance10,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(yearly_expense_vacancy)
            + float(yearly_property_mgmt)
            + float(yearly_expense_maintenance)
            + float(expense_taxes10)
            + float(yearly_expense_hoa)
            + float(expense_insurance10)
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if SumofAllExpense[count] == "undefined":  # check this condition
            SumofAllExpense[count] = 0
        total_year_calc_new_in = SumofAllIncome[count] + SumofAmountYearWise[count]
        if count == 0:
            total_year_calc_new_in = float(total_year_calc_new_in) + float(
                closing_concession
            )
        total_year_calc_new_exp = float(total_year_calc) + SumofAllExpense[count]
        total_year_calc_new = float(total_year_calc_new_in) - float(
            total_year_calc_new_exp
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + "> $ " + str(round(total_year_calc_new)) + "</td>"
        )

    result += "</tr><tr><td>CAP Rate  (NOI/Asset Acquisition Value 'AAV')</td>"
    for count in range(0, terms):
        year_leasezz = SumofAmountYearWise[count]
        yearly_expense_vacancy = expense_vacancy_calc(
            year_leasezz, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt = property_mgmt_calc(
            year_leasezz, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance = expense_maintenance_calc(
            year_leasezz, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes2 = expense_taxes_calc(
            request,
            expense_taxes2,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance2 = expense_insurance_calc(
            request,
            expense_insurance2,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(yearly_expense_vacancy)
            + float(yearly_property_mgmt)
            + float(yearly_expense_maintenance)
            + expense_taxes2
            + yearly_expense_hoa
            + expense_insurance2
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        total_year_calc_new = (
            int(SumofAllIncome[count] + SumofAmountYearWise[count])
            - int(total_year_calc)
            - int(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc_new = float(total_year_calc_new) + float(closing_concession)
        try:
            acq_value = (total_year_calc_new / balance) * 100
        except ZeroDivisionError:
            acq_value = 0
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"

        result += "<td id=" + blurcss + ">" + str(round(acq_value, 2)) + " %</td>"

    result += "</tr><tr><td>Interest Paid to Mortgage</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan1 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan1 = amort_calc(
            mortagage_loan1,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )

        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(round(payy, 0)) + "</td>"

    result += "</tr><tr><td>Net Income (NOI-Interest Paid)</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan2 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan2 = amort_calc(
            mortagage_loan2,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        year_leasezy = SumofAmountYearWise[count]
        yearly_expense_vacancy = expense_vacancy_calc(
            year_leasezy, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt = property_mgmt_calc(
            year_leasezy, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance = expense_maintenance_calc(
            year_leasezy, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes3 = expense_taxes_calc(
            request,
            expense_taxes3,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance3 = expense_insurance_calc(
            request,
            expense_insurance3,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(yearly_expense_vacancy)
            + float(yearly_property_mgmt)
            + float(yearly_expense_maintenance)
            + expense_taxes3
            + yearly_expense_hoa
            + expense_insurance3
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        total_year_calc_new_in = SumofAllIncome[count] + SumofAmountYearWise[count]
        if count == 0:
            total_year_calc_new_in = float(total_year_calc_new_in) + float(
                closing_concession
            )
        total_year_calc_new_exp = float(total_year_calc) + float(SumofAllExpense[count])
        total_year_calc_new = float(total_year_calc_new_in) - float(
            total_year_calc_new_exp
        )
        net_income = float(total_year_calc_new) - float(payy)
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + "> $ " + str(round(getNum(net_income))) + "</td>"
        )

    result += "</tr><tr><td>Principal </td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan3 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan3 = amort_calc_principal(
            mortagage_loan3,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12

        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"

        result += "<td id=" + blurcss + "> $ " + str(round(getNum(payy))) + "</td>"

    result += "</tr><tr><td>Yearly Cashflow</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    YearCashFlowFinal = 0
    mortagage_loan4 = mortagage_loan

    for count in range(0, terms):
        payz, mortagage_loan5 = amort_calc(
            mortagage_loan5,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payz = float(payz)

        year_leasemm = SumofAmountYearWise[count]
        yearly_expense_vacancy22 = expense_vacancy_calc(
            year_leasemm, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt22 = property_mgmt_calc(
            year_leasemm, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance22 = expense_maintenance_calc(
            year_leasemm, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes4 = expense_taxes_calc(
            request,
            expense_taxes4,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa22 = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance4 = expense_insurance_calc(
            request,
            expense_insurance4,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc21 = (
            float(yearly_expense_vacancy22)
            + float(yearly_property_mgmt22)
            + float(yearly_expense_maintenance22)
            + float(expense_taxes4)
            + float(yearly_expense_hoa22)
            + float(expense_insurance4)
        )
        if count == 0:
            total_year_calc21 = float(total_year_calc21) + float(closing_expenses)
        total_year_calc_new_in = SumofAllIncome[count] + SumofAmountYearWise[count]
        if count == 0:
            total_year_calc_new_in = float(total_year_calc_new_in) + float(
                closing_concession
            )
        total_year_calc_new_exp = float(total_year_calc21) + float(
            SumofAllExpense[count]
        )
        total_year_calc_new = float(total_year_calc_new_in) - float(
            total_year_calc_new_exp
        )
        net_income22 = float(total_year_calc_new) - float(payz)
        payyr, mortagage_loan4 = amort_calc_principal(
            mortagage_loan4,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payyr = float(payyr)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        yealy_cashflow = net_income22 - payyr
        YearCashFlowFinal += yealy_cashflow
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(round(yealy_cashflow)) + "</td>"

    result += "</tr><tr><td>Yearly ROI</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan8 = mortagage_loan
    total_roi = 0
    for count in range(0, terms):
        payy, mortagage_loan8 = amort_calc(
            mortagage_loan8,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        year_leasezpy = SumofAmountYearWise[count]
        yearly_expense_vacancy = expense_vacancy_calc(
            year_leasezpy, expense_vacancy_set, expense_vacancy_type
        )
        yearly_property_mgmt = property_mgmt_calc(
            year_leasezpy, property_mgmt_set, property_mgmt_type
        )
        yearly_expense_maintenance = expense_maintenance_calc(
            year_leasezpy, expense_maintenance_set, expense_maintenance_type
        )
        expense_taxes9 = expense_taxes_calc(
            request,
            expense_taxes9,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance9 = expense_insurance_calc(
            request,
            expense_insurance9,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc21 = (
            float(yearly_expense_vacancy)
            + float(yearly_property_mgmt)
            + float(yearly_expense_maintenance)
            + float(expense_taxes9)
            + float(yearly_expense_hoa)
            + float(expense_insurance9)
        )
        if count == 0:
            total_year_calc21 = float(total_year_calc21) + float(closing_expenses)
        total_year_calc_new_in = float(SumofAllIncome[count]) + float(
            SumofAmountYearWise[count]
        )
        if count == 0:
            total_year_calc_new_in = float(total_year_calc_new_in) + float(
                closing_concession
            )
        total_year_calc_new_exp = float(total_year_calc21) + float(
            SumofAllExpense[count]
        )
        total_year_calc_new = float(total_year_calc_new_in) - float(
            total_year_calc_new_exp
        )
        net_income22 = float(total_year_calc_new) - float(payy)
        try:
            ROI = (net_income22 / amount_down_payment) * 100
        except ZeroDivisionError:
            ROI = 0
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + ">" + str(round(ROI, 2)) + " % </td>"
        total_roi += ROI
        if count == 0:
            amort_dynamic_input_update["year1_roi"] = round(ROI, 2)

    amort_dynamic_input_update["total_roi_percentage"] = round(total_roi, 2)
    result += (
        "  </tr>   </tbody></table></br></br><span id='YearCashFlow' hidden>"
        + str(YearCashFlowFinal)
        + "</span> <span id='BM_10' hidden>"
        + str(mortagage_loan4)
        + "</span>"
    )
    return result, amort_dynamic_input_update


def amort1(
    request,
    no_years,
    asset_appraisal_type,
    asset_appraisal_value,
    sales_expense_type,
    sales_expense_value,
    balance,
    amount_down_payment,
    mortagage_interest,
    calcTerms_initial,
):
    amort1_dynamic_input_update = {}
    if asset_appraisal_type == 0:
        appraisal_text_display = "@" + str(asset_appraisal_value) + "%"
        proj_asset_value = (
            balance + ((balance * asset_appraisal_value) / 100) * no_years
        )
    else:
        appraisal_text_display = "@ $" + asset_appraisal_value
        proj_asset_value = balance + (asset_appraisal_value * no_years)
    if sales_expense_type == 0:
        sale_proceeds_text_display = "@" + str(sales_expense_value) + "%"
        sale_proceeds = proj_asset_value - (
            (proj_asset_value * sales_expense_value) / 100
        )
    else:
        sale_proceeds_text_display = "@ $" + sales_expense_value
        sale_proceeds = proj_asset_value - sales_expense_value

    if request.POST.get("inst_sum_yearcashflow"):
        YearCashFlow = float(request.POST.get("inst_sum_yearcashflow"))
    else:
        YearCashFlow = 0

    if request.POST.get("inst_sum_BM_10"):
        BM_10 = float(request.POST.get("inst_sum_BM_10"))
    else:
        BM_10 = 0
    interestRate = mortagage_interest
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = (no_years + 1) * 12
    balance = balance - amount_down_payment
    www = amort_calc_balance(balance, interestRate, calcTerms, startCount, endCount)
    profit_sale = sale_proceeds - www
    try:
        PerCashFlow = (YearCashFlow / amount_down_payment) * 100
    except ZeroDivisionError:
        PerCashFlow = 0
    ROI_10 = (YearCashFlow + profit_sale) - amount_down_payment
    amort1_dynamic_input_update["total_roi"] = round(ROI_10, 0)
    try:
        Per_profit = (ROI_10 / amount_down_payment) * 100
    except ZeroDivisionError:
        Per_profit = 0
    Cash_on_hand = ROI_10 + amount_down_payment
    YearCashFlow_display = "$ " + str(round(getNum(YearCashFlow)))
    PerCashFlow_display = str(round(getNum(PerCashFlow), 2)) + " %"
    proj_asset_value_display = "$ " + str(round(getNum(proj_asset_value)))
    sale_proceeds_display = "$ " + str(round(getNum(sale_proceeds)))
    www_display = "$ " + str(round(getNum(www)))
    profit_sale_display = "$ " + str(round(getNum(profit_sale)))
    ROI_10_display = "$ " + str(round(getNum(ROI_10)))
    Per_profit_display = str(round(getNum(Per_profit), 2)) + " %"
    Cash_on_hand_display = "$ " + str(round(getNum(Cash_on_hand)))

    result = '<table border="1" class="table table-sm"  width="800px" id="investment_summary"><tr>  <thead><tr> <th colspan="2">ROI SUMMARY </th></thead>'
    # begin building the return string for the display of the amort table
    result += (
        "<td>Total Cashflow 'CF' for "
        + str(no_years)
        + "</br> years (sum of yearly Cashflow)</td><td id='blurcss'> "
        + YearCashFlow_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Total %age of cashflow</br>  for "
        + str(no_years)
        + " years (CF/DowP)</td><td id='blurcss'> "
        + PerCashFlow_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Projected Asset value</br>  after "
        + str(no_years)
        + " years "
        + appraisal_text_display
        + " Appraisal</td><td id='blurcss'> "
        + proj_asset_value_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Sale Proceeds 'SP' </br> after expenses @ "
        + sale_proceeds_text_display
        + "</td><td id='blurcss'> "
        + sale_proceeds_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Balance Mortage 'BM' at</br>  the end of "
        + str(no_years)
        + " years</td><td id='blurcss'> "
        + www_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Profit from the sale </br> (SP-BM)</td><td id='blurcss'> "
        + profit_sale_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Total ROI for "
        + str(no_years)
        + " years </br> ((TI+Profit) - DowP)</td><td id='blurcss'> "
        + ROI_10_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Total %age of Profit</br> for "
        + str(no_years)
        + " years (ROI/DowP)</td><td id='blurcss'> "
        + Per_profit_display
        + "</td></tr>"
    )
    result += (
        "<tr><td>Cash on Hand after </br> "
        + str(no_years)
        + " years</td><td id='blurcss'> "
        + Cash_on_hand_display
        + "</td></tr>"
    )
    result += "</table>"
    return result, amort1_dynamic_input_update


def comm_amort(
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
    mortagage_loan,
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
    mortagage_interest,
    calcTerms_initial,
    expense_vacancy,
    expense_vacancy_type,
):
    amort_dynamic_input_update = {}
    monthlyRate = interestRate / 12
    if lease_rate_type == 0:
        year_lease = lease_rate * sft_leased
        year_lease2 = lease_rate * sft_leased
        year_lease3 = lease_rate * sft_leased
        year_lease4 = lease_rate * sft_leased
        year_leasex = lease_rate * sft_leased
        year_leasez = lease_rate * sft_leased
        year_leasezy = lease_rate * sft_leased
        year_leasey = lease_rate * sft_leased
        year_lease25 = lease_rate * sft_leased
        year_leasezz = lease_rate * sft_leased
        year_leasemm = lease_rate * sft_leased
        year_leasekk = lease_rate * sft_leased
        year_leaseyy = lease_rate * sft_leased
        year_leasenn = lease_rate * sft_leased
        year_leasezpy = lease_rate * sft_leased
        year_lease1 = lease_rate * sft_leased
        year_lease26 = lease_rate * sft_leased
    else:
        year_lease1 = lease_rate * 12
        year_lease = lease_rate * 12
        year_lease2 = lease_rate * 12
        year_lease3 = lease_rate * 12
        year_lease4 = lease_rate * 12
        year_lease1 = lease_rate * 12
        year_leasex = lease_rate * 12
        year_leasez = lease_rate * 12
        year_leasezy = lease_rate * 12
        year_leasey = lease_rate * 12
        year_lease25 = lease_rate * 12
        year_leasezz = lease_rate * 12
        year_leasemm = lease_rate * 12
        year_leasekk = lease_rate * 12
        year_leaseyy = lease_rate * 12
        year_leasenn = lease_rate * 12
        year_leasezpy = lease_rate * 12
        year_lease26 = lease_rate * 12

    mortagage_loan5 = mortagage_loan
    expense_taxes4 = expense_taxes
    expense_taxes1 = expense_taxes
    expense_taxes2 = expense_taxes
    expense_taxes3 = expense_taxes
    expense_taxes9 = expense_taxes
    expense_taxes10 = expense_taxes

    # Calculate the payment
    expense_insurance = insurance_expense
    expense_insurance1 = expense_insurance
    expense_insurance2 = expense_insurance
    expense_insurance3 = expense_insurance
    expense_insurance4 = expense_insurance
    expense_insurance9 = expense_insurance

    result = ""
    result += "<table border='1' class='table table-sm'   width='1000px' id='investment_analysis' ><thead> <tr>  "
    result += "<th>Tenant Name</th>"
    for count in range(0, terms):
        result += "<th id='Year'>Year " + str(count + 1) + " Lease</th>"

    tenant_list = request.POST.getlist("tenant_name")
    sft_leased_list = request.POST.getlist("sft_leased")
    lease_rate_type_list = request.POST.getlist("lease_rate_type")
    lease_rate_list = request.POST.getlist("lease_rate")
    rent_frequency_list = request.POST.getlist("rent_frequency")
    rent_increases_list = request.POST.getlist("rent_increases")
    rent_increase_value_list = request.POST.getlist("rent_increase_value")
    rent_increases_for_every_year_list = request.POST.getlist(
        "rent_increases_for_every_year"
    )

    SumofAmountYearWise = []

    for i in range(0, len(tenant_list)):
        if lease_rate_type == 0:
            year_lease1 = sft_leased_list[i] * lease_rate_list[i]
        else:
            year_lease1 = lease_rate_list[i] * 12
        result += " </tr></thead><tbody> <tr><td>" + tenant_list[i] + "</td>"
        lease_rate = lease_rate_list[i]
        for count in range(0, terms):
            if int(rent_frequency_list[i]) == 1:
                count2 = count + 1
            else:
                count2 = count
            tenant_count = i
            lease_rate = year_lease_calc2(request, lease_rate, count2, tenant_count)
            if not lease_rate:
                lease_rate = 0
            if int(lease_rate_type_list[i]) == 1:
                year_lease2 = lease_rate * 12
            else:
                if sft_leased_list[i]:
                    year_lease2 = float(lease_rate) * float(sft_leased_list[i])
                else:
                    year_lease2 = float(lease_rate) * 0
            if i == 0:
                SumofAmountYearWise.append(year_lease2)  # 10
            else:
                SumofAmountYearWise[count] = SumofAmountYearWise[count] + year_lease2
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"
            result += (
                "<td id=" + blurcss + "> $ " + str(round(year_lease2, 0)) + "</td>"
            )

    ####Additional Incomes#####
    additional_income_nums = request.POST.get("additional_income_nums").split(",")
    income_name_list = request.POST.getlist("income_name")
    # print("income_name_list", income_name_list)
    income_amount_list = request.POST.getlist("income_amount")
    income_frequency_list = request.POST.getlist("income_frequency")
    SumofAllIncome = []
    for i in range(0, len(income_name_list)):
        income_increases_type_list = request.POST.getlist(
            "income_increases_type[" + str(additional_income_nums[i]) + "]"
        )
        income_increase_value_list = request.POST.getlist(
            "income_increase_value[" + str(additional_income_nums[i]) + "]"
        )
        income_increases_for_every_year_list = request.POST.getlist(
            "income_increases_for_every_year[" + str(additional_income_nums[i]) + "]"
        )

        result += (
            " </tr></thead><tbody> <tr><td>Additional Incomes - "
            + str(income_name_list[i])
            + "</td>"
        )
        for count in range(0, terms):
            if count == 0:
                if income_amount_list[i]:
                    income_amount = income_amount_list[i]
                else:
                    income_amount = 0
            additional_income_count = i
            income_amount = additional_income_calc(
                request,
                int(income_amount),
                int(income_frequency_list[i]),
                int(income_increases_type_list[0]),
                int(income_increase_value_list[0]),
                int(income_increases_for_every_year_list[0]),
                count,
                additional_income_count,
            )

            if i == 0:
                SumofAllIncome.append(income_amount)
            else:
                SumofAllIncome[count] = SumofAllIncome[count] + income_amount
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"
            result += (
                "<td id="
                + blurcss
                + "> $ "
                + str(round(float(income_amount), 0))
                + "</td>"
            )
    ####End Additional Incomes#####

    result += "</tr><tr><td>Closing Concession</td>"
    for count in range(0, terms):
        if count == 0:
            clos_conc = closing_concession
        else:
            clos_conc = 0
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(clos_conc) + " </td>"

    result += "</tr><tr><td>Total Reimbursements</td>"
    for count in range(0, terms):
        reimbursement_income1 = reimbursement_income
        reimbursement_income1 = reimbursement_calc(
            request,
            reimbursement_income1,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(float(getNum(reimbursement_income1)), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Income - Yearly Total Rents</td>"
    for count in range(0, terms):
        reimbursement_income2 = reimbursement_income
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0

        reimbursement_income2 = reimbursement_calc(
            request,
            reimbursement_income2,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        if count == 0:
            all_income_slab = (
                float(SumofAllIncome[count])
                + float(SumofAmountYearWise[count])
                + float(reimbursement_income2)
                + float(closing_concession)
            )
        else:
            all_income_slab = (
                float(SumofAllIncome[count])
                + float(SumofAmountYearWise[count])
                + float(reimbursement_income2)
            )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(all_income_slab), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expenses - Taxes</td>"
    for count in range(0, terms):
        expense_taxes_ET = expense_taxes
        expense_taxes_ET = expense_taxes_calc(
            request,
            expense_taxes_ET,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_taxes_ET), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expenses - Insurance</td>"
    for count in range(0, terms):
        expense_insurance_EI = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_insurance_EI), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expense - Common Area Maintenance</td>"
    for count in range(0, terms):
        expense_cam_CAM = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_cam_CAM), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expense - Utilities</td>"
    for count in range(0, terms):
        expense_utilities_EU = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_utilities_EU), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expense - HOA</td>"
    for count in range(0, terms):
        expense_hoa_HOA = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_hoa_HOA), 0))
            + "</td>"
        )

    if expense_vacancy_type == 0:
        expense_vacancy_type_disp = "%"
    else:
        expense_vacancy_type_disp = "$"
    result += (
        "</tr><tr><td>Expenses - Vacancy @"
        + str(expense_vacancy)
        + " "
        + str(expense_vacancy_type_disp)
        + "</td>"
    )
    for count in range(0, terms):
        reimbursement_income7 = reimbursement_income
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0
        reimbursement_income7 = reimbursement_calc(
            request,
            reimbursement_income7,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income7)
        )
        all_income_slab = int(all_income_slab)
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(float(getNum(expense_vacancy121)), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expense - Management Fee</td>"
    for count in range(0, terms):
        expense_management_EMF = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_management_EMF), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Expense - Administrative Fee</td>"
    for count in range(0, terms):
        expense_administrative_EAF = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(expense_administrative_EAF), 0))
            + "</td>"
        )

    ###Additional Expenses####
    expense_head_name_list = request.POST.getlist("expense_head_name")
    expense_amount_list = request.POST.getlist("expense_amount")
    expense_frequency_list = request.POST.getlist("expense_frequency")
    additional_expenses_nums = request.POST.get("additional_expenses_nums").split(",")
    SumofAllExpense = []
    for i in range(0, len(expense_head_name_list)):
        expense_increases_type_list = request.POST.getlist(
            "expense_increases_type[" + str(additional_expenses_nums[i]) + "]"
        )
        expense_increase_value_list = request.POST.getlist(
            "expense_increase_value[" + str(additional_expenses_nums[i]) + "]"
        )
        expense_increases_for_every_year_list = request.POST.getlist(
            "expense_increases_for_every_year[" + str(additional_expenses_nums[i]) + "]"
        )

        result += (
            " </tr></thead><tbody> <tr><td>Additional Expenses - "
            + str(expense_head_name_list[i])
            + "</td>"
        )
        for count in range(0, terms):
            if count == 0:
                if expense_amount_list[i]:
                    expense_amount = float(expense_amount_list[i])
                else:
                    expense_amount = 0
            additional_expenses_count = i
            expense_amount = additional_expense_calc(
                request,
                expense_amount,
                int(expense_frequency_list[i]),
                int(expense_increases_type_list[0]),
                int(expense_increase_value_list[0]),
                int(expense_increases_for_every_year_list[0]),
                count,
                additional_expenses_count,
            )
            if i == 0:
                SumofAllExpense.append(expense_amount)  # 10
            else:
                SumofAllExpense[count] = SumofAllExpense[count] + expense_amount
            if count > 1:
                blurcss = "blurcss"
            else:
                blurcss = "Year"

            result += (
                "<td id="
                + blurcss
                + "> $ "
                + str(round(float(expense_amount)))
                + "</td>"
            )
    ###End of Additional Expenses####

    result += "</tr><tr><td>Closing Expenses</td>"
    for count in range(0, terms):
        if count == 0:
            clos_exp = closing_expenses
        else:
            clos_exp = 0

        result += "<td id=" + blurcss + "> $ " + str(clos_exp) + " </td>"

    result += "</tr><tr><td>Total Expenses</td>"
    for count in range(0, terms):
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0
        if SumofAllExpense[count] == "undefined":
            SumofAllExpense[count] = 0
        reimbursement_income7 = reimbursement_income
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0
        reimbursement_income7 = reimbursement_calc(
            request,
            reimbursement_income7,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income7)
        )
        all_income_slab = int(all_income_slab)
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )

        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(total_year_calc), 0))
            + "</td>"
        )

    result += "</tr><tr id='noirow'><td>NOI (Yearly Total - Expenses)</td>"
    for count in range(0, terms):
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0
        if SumofAllExpense[count] == "undefined":
            SumofAllExpense[count] = 0
        reimbursement_income7 = reimbursement_income
        if SumofAllIncome[count] == "undefined":
            SumofAllIncome[count] = 0
        reimbursement_income7 = reimbursement_calc(
            request,
            reimbursement_income7,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income7)
        )
        all_income_slab = float(all_income_slab)
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if count == 0:
            all_income_slab = float(all_income_slab) + float(closing_concession)
        total_year_calc_new = float(all_income_slab) - float(total_year_calc)
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"

        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(total_year_calc_new)))
            + "</td>"
        )

    result += (
        "</tr><tr id='caprow'><td>CAP Rate  (NOI/Asset Acquisition Value 'AAV')</td>"
    )
    for count in range(0, terms):
        reimbursement_income4 = reimbursement_income
        reimbursement_income4 = reimbursement_calc(
            request,
            reimbursement_income4,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income4)
        )
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if count == 0:
            all_income_slab = float(all_income_slab) + float(closing_concession)
        total_year_calc_new = float(all_income_slab) - float(total_year_calc)
        try:
            acq_value = (total_year_calc_new / balance) * 100
        except ZeroDivisionError:
            acq_value = 0
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + ">" + str(round(getNum(acq_value), 2)) + " %</td>"
        )

    result += "</tr><tr><td>Interest Paid to Mortgage</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan1 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan1 = amort_calc(
            mortagage_loan1,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )

        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + "> $ " + str(round(payy, 0)) + "</td>"

    result += "</tr><tr><td>Net Income (NOI-Interest Paid)</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan2 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan2 = amort_calc(
            mortagage_loan2,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        reimbursement_income5 = reimbursement_income
        reimbursement_income5 = reimbursement_calc(
            request,
            reimbursement_income5,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income5)
        )
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if count == 0:
            all_income_slab = float(all_income_slab) + float(closing_concession)
        total_year_calc_new = float(all_income_slab) - float(total_year_calc)
        net_income = float(total_year_calc_new) - float(payy)
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id=" + blurcss + "> $ " + str(round(getNum(net_income), 0)) + "</td>"
        )

    result += "</tr><tr><td>Principal </td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan3 = mortagage_loan
    for count in range(0, terms):
        payy, mortagage_loan3 = amort_calc_principal(
            mortagage_loan3,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12

        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"

        result += "<td id=" + blurcss + "> $ " + str(round(getNum(payy))) + "</td>"

    result += "</tr><tr><td>Yearly Cashflow</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    YearCashFlowFinal = 0
    mortagage_loan4 = mortagage_loan

    for count in range(0, terms):
        payz, mortagage_loan5 = amort_calc(
            mortagage_loan5,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payz = float(payz)
        reimbursement_income6 = reimbursement_income
        reimbursement_income6 = reimbursement_calc(
            request,
            reimbursement_income6,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income6)
        )
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if count == 0:
            all_income_slab = float(all_income_slab) + float(closing_concession)
        total_year_calc_new = float(all_income_slab) - float(total_year_calc)
        net_income22 = total_year_calc_new - payz
        payyr, mortagage_loan4 = amort_calc_principal(
            mortagage_loan4,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payyr = float(payyr)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        yealy_cashflow = net_income22 - payyr
        YearCashFlowFinal += yealy_cashflow
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + "> $ "
            + str(round(getNum(yealy_cashflow), 0))
            + "</td>"
        )

    result += "</tr><tr><td>Yearly ROI</td>"
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = 12
    mortagage_loan8 = mortagage_loan
    total_roi = 0
    for count in range(0, terms):
        payy, mortagage_loan8 = amort_calc(
            mortagage_loan8,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payy = float(payy)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        reimbursement_income9 = reimbursement_income
        reimbursement_income9 = reimbursement_calc(
            request,
            reimbursement_income9,
            reim_ye_mo,
            reim_frequency,
            reim_increases_type,
            reim_increase_value,
            reim_increases_for_every_year,
            count,
        )
        all_income_slab = (
            float(SumofAllIncome[count])
            + float(SumofAmountYearWise[count])
            + float(reimbursement_income9)
        )
        expense_vacancy121 = expense_vacancy
        expense_vacancy121 = expense_vacancy_calc(
            all_income_slab, expense_vacancy121, expense_vacancy_type
        )
        expense_cam_TE = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_TE = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_TE = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_TE = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_TE = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_TE = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_TE = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            float(expense_vacancy121)
            + float(expense_cam_TE)
            + float(expense_utilities_TE)
            + float(expense_management_TE)
            + float(expense_administrative_TE)
            + float(expense_taxes_TE)
            + float(yearly_expense_hoa_TE)
            + float(expense_insurance_TE)
            + float(SumofAllExpense[count])
        )
        if count == 0:
            total_year_calc = float(total_year_calc) + float(closing_expenses)
        if count == 0:
            all_income_slab = float(all_income_slab) + float(closing_concession)
        total_year_calc_new = float(all_income_slab) - float(total_year_calc)
        net_income = total_year_calc_new - payy
        try:
            ROI = float(net_income) / float(amount_down_payment) * 100
        except ZeroDivisionError:
            ROI = 0
        total_roi += ROI
        if count == 0:
            amort_dynamic_input_update["year1_roi"] = round(ROI, 2)
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += "<td id=" + blurcss + ">" + str(round(getNum(ROI), 2)) + "% </td>"

    result += "</tr><tr><td>Debt Service Ratio</td>"
    for count in range(0, terms):
        year_leasez = int(SumofAllIncome[count]) + int(SumofAmountYearWise[count])
        expense_cam_DSR = cam_calc(
            request,
            expense_cam,
            cam_ye_mo,
            cam_frequency,
            cam_increases_type,
            cam_increase_value,
            cam_increases_for_every_year,
            count,
        )
        expense_utilities_DSR = utilities_calc(
            request,
            expense_utilities,
            utilities_ye_mo,
            utilities_frequency,
            utilities_increases_type,
            utilities_increase_value,
            utilities_increases_for_every_year,
            count,
        )
        expense_management_DSR = management_calc(
            request,
            expense_management,
            management_ye_mo,
            management_frequency,
            management_increases_type,
            management_increase_value,
            management_increases_for_every_year,
            count,
        )
        expense_administrative_DSR = administrative_calc(
            request,
            expense_administrative,
            administrative_ye_mo,
            administrative_frequency,
            administrative_increases_type,
            administrative_increase_value,
            administrative_increases_for_every_year,
            count,
        )
        expense_taxes_DSR = expense_taxes_calc(
            request,
            expense_taxes,
            taxes_ye_mo,
            taxes_frequency,
            taxes_increases_type,
            taxes_increase_value,
            taxes_increases_for_every_year,
            count,
        )
        yearly_expense_hoa_DSR = hoa_calc(
            request,
            expense_hoa,
            hoa_ye_mo,
            hoa_frequency,
            hoa_increases_type,
            hoa_increase_value,
            hoa_increases_for_every_year,
            count,
        )
        expense_insurance_DSR = expense_insurance_calc(
            request,
            expense_insurance,
            insu_ye_mo,
            insu_frequency,
            insu_increases_type,
            insu_increase_value,
            insu_increases_for_every_year,
            count,
        )
        total_year_calc = (
            expense_cam_DSR
            + expense_utilities_DSR
            + expense_management_DSR
            + expense_administrative_DSR
            + expense_taxes_DSR
            + yearly_expense_hoa_DSR
            + expense_insurance_DSR
        )
        TR = (
            expense_cam_DSR
            + expense_utilities_DSR
            + expense_management_DSR
            + expense_taxes_DSR
            + yearly_expense_hoa_DSR
            + expense_insurance_DSR
        )
        total_year_calc_DSR = year_leasez - total_year_calc + TR
        total_year_calc_DSR = total_year_calc_DSR * float(debt_service_ratio)
        calcTerms = calcTerms_initial
        startCount = 1
        endCount = 12
        mortagage_loan1 = mortagage_loan
        payDSR, mortagage_loan1 = amort_calc(
            mortagage_loan1,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payDSR = float(payDSR)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        calcTerms = calcTerms_initial
        startCount = 1
        endCount = 12
        mortagage_loan3 = mortagage_loan
        payP_DSR, mortagage_loan3 = amort_calc_principal(
            mortagage_loan3,
            mortagage_interest,
            count + 1,
            calcTerms,
            startCount,
            endCount,
        )
        payP_DSR = float(payP_DSR)
        calcTerms = calcTerms - 12
        startCount = endCount + 1
        endCount = endCount + 12
        total_DSR = payP_DSR + payDSR
        try:
            total_DSR_final = total_year_calc_DSR / total_DSR
        except ZeroDivisionError:
            total_DSR_final = 0
        if count > 1:
            blurcss = "blurcss"
        else:
            blurcss = "Year"
        result += (
            "<td id="
            + blurcss
            + ">"
            + str(round(getNum(total_DSR_final), 2))
            + " %</td>"
        )

    amort_dynamic_input_update["total_roi_percentage"] = round(total_roi, 2)
    result += (
        "  </tr>   </tbody></table></br></br><span id='YearCashFlow' hidden>"
        + str(YearCashFlowFinal)
        + "</span> <span id='BM_10' hidden>"
        + str(mortagage_loan4)
        + "</span>"
    )
    return result, amort_dynamic_input_update


def comm_amort1(
    request,
    no_years,
    asset_appraisal_type,
    asset_appraisal_value,
    sales_expense_type,
    sales_expense_value,
    balance,
    amount_down_payment,
    mortagage_interest,
    calcTerms_initial,
):
    amort1_dynamic_input_update = {}
    if asset_appraisal_type == 0:
        appraisal_text_display = "@" + str(asset_appraisal_value) + "%"
        proj_asset_value = (
            balance + ((balance * asset_appraisal_value) / 100) * no_years
        )
    else:
        appraisal_text_display = "@ $" + asset_appraisal_value
        proj_asset_value = balance + (asset_appraisal_value * no_years)

    if request.POST.get("inst_sum_yearcashflow"):
        YearCashFlow = float(request.POST.get("inst_sum_yearcashflow"))
    else:
        YearCashFlow = 0

    if request.POST.get("inst_sum_BM_10"):
        BM_10 = float(request.POST.get("inst_sum_BM_10"))
    else:
        BM_10 = 0
    interestRate = mortagage_interest
    calcTerms = calcTerms_initial
    startCount = 1
    endCount = (no_years + 1) * 12
    balance = balance - amount_down_payment
    www = amort_calc_balance(balance, interestRate, calcTerms, startCount, endCount)
    profit_sale = sale_proceeds - www
    try:
        PerCashFlow = (YearCashFlow / amount_down_payment) * 100
    except ZeroDivisionError:
        PerCashFlow = 0
    ROI_10 = (YearCashFlow + profit_sale) - amount_down_payment
    noi_string = request.POST.get("noi_value")
    noi_string = noi_string.replace("$", "")
    noi_val = float(noi_string.replace(",", ""))
    cap_string = request.POST.get("cap_value")
    cap_val = float(cap_string.replace("%", ""))
    capf_string = request.POST.get("capf_value")
    cap = (noi_val / cap_val) * 100
    proj_asset_value_10 = float(proj_asset_value) + float(cap)
    if sales_expense_type == 0:
        sale_proceeds_text_display = "@" + str(sales_expense_value) + "%"
        sale_proceeds = proj_asset_value_10 - (
            (proj_asset_value_10 * sales_expense_value) / 100
        )
    else:
        sale_proceeds_text_display = "@ $" + sales_expense_value
        sale_proceeds = proj_asset_value_10 - sales_expense_value
    profit_sale = sale_proceeds - www
    total_roi = (YearCashFlow + profit_sale) - amount_down_payment
    try:
        Per_profit = (total_roi / amount_down_payment) * 100
    except ZeroDivisionError:
        Per_profit = 0
    Cash_on_hand = total_roi + amount_down_payment
    amort1_dynamic_input_update["total_roi"] = round(total_roi)

    if YearCashFlow:
        YearCashFlow_display = "$ " + str(round(getNum(YearCashFlow)))
    else:
        YearCashFlow_display = ""
    if PerCashFlow:
        PerCashFlow_display = str(round(PerCashFlow)) + " %"
    else:
        PerCashFlow_display = ""
    if proj_asset_value:
        proj_asset_value_display = "$ " + str(round(getNum(proj_asset_value)))
    else:
        proj_asset_value_display = ""
    if sale_proceeds:
        sale_proceeds_display = "$ " + str(round(getNum(sale_proceeds)))
    else:
        sale_proceeds_display = ""
    if www:
        www_display = "$ " + str(round(getNum(www)))
    else:
        www_display = ""
    if profit_sale:
        profit_sale_display = "$ " + str(round(getNum(profit_sale)))
    else:
        profit_sale_display = ""
    if ROI_10:
        ROI_10_display = "$ " + str(round(getNum(total_roi)))
    else:
        ROI_10_display = ""
    if Per_profit:
        Per_profit_display = str(round(Per_profit, 2)) + " %"
    else:
        Per_profit_display = ""
    if Cash_on_hand:
        Cash_on_hand_display = "$ " + str(round(getNum(Cash_on_hand)))
    else:
        Cash_on_hand_display = ""

    result = '<table border="1" class="table table-sm"  width="800px" id="investment_summary"><tr>  <thead><tr> <th colspan="2">ROI SUMMARY </th></thead>'
    result += (
        "<td>Total Cashflow 'CF' for "
        + str(no_years)
        + "</br> years (sum of yearly Cashflow)</td><td id='blurcss'> $ "
        + str(round(getNum(YearCashFlow)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Total %age of cashflow</br>  for "
        + str(no_years)
        + " years (CF/DowP)</td><td id='blurcss'> "
        + str(round(getNum(PerCashFlow), 2))
        + " %</td></tr>"
    )
    result += (
        "<tr><td>CAP Based Asset value after </br>  "
        + str(no_years)
        + " years @"
        + str(cap_string)
        + " CAP</td><td id='blurcss'> $ "
        + str(round(getNum(cap)))
        + " </td></tr>"
    )
    result += (
        "<tr><td>Increase Asset value</br>  after "
        + str(no_years)
        + " years "
        + appraisal_text_display
        + " Appraisal</td><td id='blurcss'> $ "
        + str(round(getNum(proj_asset_value)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Projected Asset value</br>  after "
        + str(no_years)
        + " years </td><td id='blurcss'> $ "
        + str(round(getNum(proj_asset_value_10)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Sale Proceeds 'SP' </br> after expenses "
        + sale_proceeds_text_display
        + "</td><td id='blurcss'> $ "
        + str(round(getNum(sale_proceeds)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Balance Mortage 'BM' at</br>  the end of "
        + str(no_years)
        + " years</td><td id='blurcss'> $ "
        + str(round(getNum(www)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Profit from the sale </br> (SP-BM)</td><td id='blurcss'> $ "
        + str(round(getNum(profit_sale)))
        + "</td></tr>"
    )
    result += (
        "<tr id='final_total_roi'><td>Total ROI for "
        + str(no_years)
        + " years </br> ((TI+Profit) - DowP)</td><td id='blurcss'>$ "
        + str(round(getNum(total_roi)))
        + "</td></tr>"
    )
    result += (
        "<tr><td>Total %age of Profit</br> for "
        + str(no_years)
        + " years (ROI/DowP)</td><td id='blurcss'> "
        + str(round(getNum(Per_profit), 2))
        + " %</td></tr>"
    )
    result += (
        "<tr><td>Cash on Hand after </br> "
        + str(no_years)
        + " years</td><td id='blurcss'> $ "
        + str(round(getNum(Cash_on_hand)))
        + "</td></tr>"
    )
    result += "</table>"
    return result, amort1_dynamic_input_update


def validateInputs(value):
    # some code here to validate inputs
    if (value == None) or (value == ""):
        return False
    else:
        return True


def year_lease_calc2(request, lease_rate, count, tenant_count):
    # print("ENTERED YEAR LEASE CALC2")
    tenant_nums = request.POST.get("tenant_nums").split(
        ","
    )  # getting tenant numbers of rowt0

    rent_frequency_list = request.POST.getlist("rent_frequency")

    rent_increase_value_list = request.POST.getlist(
        "rent_increase_value[" + str(tenant_nums[tenant_count]) + "]"
    )
    rent_increases_list = request.POST.getlist(
        "rent_increases[" + str(tenant_nums[tenant_count]) + "]"
    )
    rent_increases_for_every_year_list = request.POST.getlist(
        "rent_increases_for_every_year[" + str(tenant_nums[tenant_count]) + "]"
    )

    sft_leased_list = request.POST.getlist("sft_leased")

    lease_rate_type_list = request.POST.getlist("lease_rate_type")

    for i in range(0, len(rent_increase_value_list)):
        if int(rent_frequency_list[tenant_count]) == 0:
            if int(rent_increases_list[i]) == 0:
                if (
                    count % int(rent_increases_for_every_year_list[i]) == 0
                ) and count != 0:
                    lease_rate = (
                        float(lease_rate)
                        + float(lease_rate) * float(rent_increase_value_list[i]) * 0.01
                    )

            else:
                if (
                    count % int(rent_increases_for_every_year_list[i]) == 0
                    and count != 0
                ):
                    lease_rate = float(lease_rate) + float(rent_increase_value_list[i])
        else:
            if int(rent_increases_list[i]) == 0:
                if (count == int(rent_increases_for_every_year_list[i])) and count != 1:
                    lease_rate = float(lease_rate) + float(
                        float(lease_rate) * float(rent_increase_value_list[i]) * 0.01
                    )
            else:
                if (count == int(rent_increases_for_every_year_list[i])) and count != 1:
                    lease_rate = float(lease_rate) + float(rent_increase_value_list[i])

        return lease_rate


def additional_income_calc(
    request,
    amount,
    income_frequency,
    income_increases_type,
    income_increase_value,
    income_increases_for_every_year,
    count,
    additional_income_count,
):
    global income_amount
    if income_frequency == 0:
        if income_increases_type == 0:
            if count == 0:
                income_amount = amount * 1
            elif count % income_increases_for_every_year == 0:
                income_increase_value = 1 + income_increase_value * 0.01
                income_amount = income_amount * income_increase_value
            else:
                income_amount = income_amount * 1
        else:
            if count == 0:
                income_amount = amount * 1
            elif count % income_increases_for_every_year == 0:
                income_amount = int(income_amount) + int(income_increase_value)
            else:
                income_amount = income_amount * 1
    else:
        additional_income_nums = request.POST.get("additional_income_nums").split(
            ","
        )  # getting addtional income numbers of rowa0
        income_increases_list = request.POST.getlist(
            "income_increases_type["
            + str(additional_income_nums[additional_income_count])
            + "]"
        )
        income_increase_value_list = request.POST.getlist(
            "income_increase_value["
            + str(additional_income_nums[additional_income_count])
            + "]"
        )
        income_increases_for_every_year_list = request.POST.getlist(
            "income_increases_for_every_year["
            + str(additional_income_nums[additional_income_count])
            + "]"
        )
        for i in range(0, len(income_increase_value_list)):
            actual = int(income_increases_for_every_year_list[i]) - 1
            if income_increases_list[i] == 0:
                if count == 0:
                    income_amount = amount * 1
                elif count == actual:
                    income_increase_value = 1 + income_increase_value_list[i] * 0.01
                    income_amount = income_amount * income_increase_value
                else:
                    income_amount = income_amount * 1
            else:
                if count == 0:
                    income_amount = amount * 1
                elif count == actual:
                    income_amount = int(income_amount) + int(
                        income_increase_value_list[i]
                    )
                else:
                    income_amount = income_amount * 1

    return income_amount


def expense_taxes_calc(
    request,
    taxes,
    taxes_ye_mo,
    taxes_frequency,
    taxes_increases_type,
    taxes_increase_value,
    taxes_increases_for_every_year,
    count,
):
    global expense_taxes
    if taxes_frequency == 0:
        if taxes_increases_type == 0:
            if count == 0:
                expense_taxes = taxes * 1
            elif count % taxes_increases_for_every_year == 0:
                taxes_increase_value = 1 + taxes_increase_value * 0.01
                expense_taxes = expense_taxes * taxes_increase_value
            else:
                expense_taxes = expense_taxes * 1
        else:
            if count == 0:
                expense_taxes = taxes * 1
            elif count % taxes_increases_for_every_year == 0:
                expense_taxes = int(expense_taxes) + int(taxes_increase_value)
            else:
                expense_taxes = expense_taxes * 1
    else:
        taxes_increases_type_list = request.POST.getlist("taxes_increases_type")
        taxes_increase_value_list = request.POST.getlist("taxes_increase_value")
        taxes_increases_for_every_year_list = request.POST.getlist(
            "taxes_increases_for_every_year"
        )
        for i in range(0, len(taxes_increase_value_list)):
            if not taxes_increase_value_list[i]:
                taxes_increase_value_list[i] = 0
            actual_taxes = int(taxes_increases_for_every_year_list[i]) - 1
            if int(taxes_increases_type_list[i]) == 0:
                if count == 0:
                    expense_taxes = taxes * 1
                elif count == actual_taxes:
                    taxes_increase_value = (
                        1 + float(taxes_increase_value_list[i]) * 0.01
                    )
                    expense_taxes = expense_taxes * taxes_increase_value
                else:
                    expense_taxes = expense_taxes * 1
            else:
                if count == 0:
                    expense_taxes = taxes * 1
                elif count == actual_taxes:
                    expense_taxes = float(expense_taxes) + float(
                        taxes_increase_value_list[i]
                    )
                else:
                    expense_taxes = expense_taxes * 1
    if taxes_ye_mo == 0:
        return expense_taxes
    else:
        return expense_taxes * 12


def expense_insurance_calc(
    request,
    insu,
    insu_ye_mo,
    insu_frequency,
    insu_increases_type,
    insu_increase_value,
    insu_increases_for_every_year,
    count,
):
    global expense_insu
    if insu_frequency == 0:
        if insu_increases_type == 0:
            if count == 0:
                expense_insu = insu * 1
            elif count % insu_increases_for_every_year == 0:
                insu_increase_value = 1 + insu_increase_value * 0.01
                expense_insu = expense_insu * insu_increase_value
            else:
                expense_insu = expense_insu * 1
        else:
            if count == 0:
                expense_insu = insu * 1
            elif count % insu_increases_for_every_year == 0:
                expense_insu = int(expense_insu) + int(insu_increase_value)
            else:
                expense_insu = expense_insu * 1
    else:
        insu_increases_type_list = request.POST.getlist("insu_increases_type")
        insu_increase_value_list = request.POST.getlist("insu_increase_value")
        insu_increases_for_every_year_list = request.POST.getlist(
            "insu_increases_for_every_year"
        )
        for i in range(0, len(insu_increase_value_list)):
            if not insu_increase_value_list[i]:
                insu_increase_value_list[i] = 0
            actual = int(insu_increases_for_every_year_list[i]) - 1
            if int(insu_increases_type_list[i]) == 0:
                if count == 0:
                    expense_insu = insu * 1
                elif count == actual:
                    insu_increase_value = 1 + float(insu_increase_value_list[i]) * 0.01
                    expense_insu = expense_insu * insu_increase_value
                else:
                    expense_insu = expense_insu * 1
            else:
                if count == 0:
                    expense_insu = insu * 1
                elif count == actual:
                    expense_insu = int(expense_insu) + int(insu_increase_value_list[i])
                else:
                    expense_insu = expense_insu * 1
    if insu_ye_mo == 0:
        return expense_insu
    else:
        return expense_insu * 12


def hoa_calc(
    request,
    hoa,
    hoa_ye_mo,
    hoa_frequency,
    hoa_increases_type,
    hoa_increase_value,
    hoa_increases_for_every_year,
    count,
):
    global expense_hoa
    if hoa_frequency == 0:
        if hoa_increases_type == 0:
            if count == 0:
                expense_hoa = hoa * 1
            elif count % hoa_increases_for_every_year == 0:
                hoa_increase_value = 1 + hoa_increase_value * 0.01
                expense_hoa = expense_hoa * hoa_increase_value
            else:
                expense_hoa = expense_hoa * 1
        else:
            if count == 0:
                expense_hoa = hoa * 1
            elif count % hoa_increases_for_every_year == 0:
                expense_hoa = int(expense_hoa) + int(hoa_increase_value)
            else:
                expense_hoa = expense_hoa * 1
    else:
        hoa_increases_type_list = request.POST.getlist("hoa_increases_type")
        hoa_increase_value_list = request.POST.getlist("hoa_increase_value")
        hoa_increases_for_every_year_list = request.POST.getlist(
            "hoa_increases_for_every_year"
        )
        for i in range(0, len(hoa_increase_value_list)):
            if not hoa_increase_value_list[i]:
                hoa_increase_value_list[i] = 0
            actual_hoa = int(hoa_increases_for_every_year_list[i]) - 1
            if int(hoa_increases_type_list[i]) == 0:
                if count == 0:
                    expense_hoa = hoa * 1
                elif count == actual_hoa:
                    hoa_increase_value = 1 + float(hoa_increase_value_list[i]) * 0.01
                    expense_hoa = expense_hoa * hoa_increase_value
                else:
                    expense_hoa = expense_hoa * 1
            else:
                if count == 0:
                    expense_hoa = hoa * 1
                elif count == actual_hoa:
                    expense_hoa = int(expense_hoa) + int(hoa_increase_value_list[i])
                else:
                    expense_hoa = expense_hoa * 1

    if hoa_ye_mo == 0:
        return expense_hoa
    else:
        return expense_hoa * 12


def expense_maintenance_calc(
    year_lease2, expense_maintenance_set, expense_maintenance_type
):
    if expense_maintenance_type == 0:
        expense_maintenance = year_lease2 * 0.01 * expense_maintenance_set
    else:
        expense_maintenance = expense_maintenance_set

    return expense_maintenance


def expense_vacancy_calc(year_lease, expense_vacancy_set, expense_vacancy_type):
    if expense_vacancy_type == 0:
        expense_vacancy = year_lease * 0.01 * expense_vacancy_set
    else:
        expense_vacancy = expense_vacancy_set
    return expense_vacancy


def property_mgmt_calc(year_lease, property_mgmt_set, property_mgmt_type):
    if property_mgmt_type == 0:
        property_mgmt = year_lease * 0.01 * property_mgmt_set
    else:
        property_mgmt = property_mgmt_set
    return property_mgmt


def additional_expense_calc(
    request,
    amount,
    expense_frequency,
    expense_increases_type,
    expense_increase_value,
    expense_increases_for_every_year,
    count,
    additional_expenses_count,
):
    global expense_amount
    if expense_frequency == 0:
        if expense_increases_type == 0:
            if count == 0:
                expense_amount = amount * 1
            elif count % expense_increases_for_every_year == 0:
                expense_increase_value = 1 + expense_increase_value * 0.01
                expense_amount = expense_amount * expense_increase_value
            else:
                expense_amount = expense_amount * 1
        else:
            if count == 0:
                expense_amount = amount * 1
            elif count % expense_increases_for_every_year == 0:
                expense_amount = int(expense_amount) + int(expense_increase_value)
            else:
                expense_amount = expense_amount * 1
    else:
        additional_expenses_nums = request.POST.get("additional_expenses_nums").split(
            ","
        )  # getting addtional iexpenses numbers of rowe0
        expense_increases_list = request.POST.getlist(
            "expense_increases_type["
            + str(additional_expenses_nums[additional_expenses_count])
            + "]"
        )
        expense_increase_value_list = request.POST.getlist(
            "expense_increase_value["
            + str(additional_expenses_nums[additional_expenses_count])
            + "]"
        )
        expense_increases_for_every_year_list = request.POST.getlist(
            "expense_increases_for_every_year["
            + str(additional_expenses_nums[additional_expenses_count])
            + "]"
        )
        for i in range(0, len(expense_increase_value_list)):
            actual = int(expense_increases_for_every_year_list[i]) - 1
            if int(expense_increases_list[i]) == 0:
                if count == 0:
                    expense_amount = amount * 1
                elif count == actual:
                    expense_increase_value = (
                        1 + int(expense_increase_value_list[i]) * 0.01
                    )
                    expense_amount = expense_amount * expense_increase_value
                else:
                    expense_amount = expense_amount * 1
            else:
                if count == 0:
                    expense_amount = expense_amount * 1
                elif count == actual:
                    expense_amount = int(expense_amount) + int(
                        expense_increase_value_list[i]
                    )
                else:
                    expense_amount = expense_amount * 1

    return expense_amount


def amort_calc(balance, interestRate, countingYears, terms, startCount, endCount):
    monthlyRate = interestRate / 12
    monthlyRate = monthlyRate * 0.01
    interest = 0
    finalInstr = 0
    monthlyPrincipal = 0
    try:
        payment = balance * (monthlyRate / (1 - math.pow(1 + monthlyRate, -terms)))
    except ZeroDivisionError:
        payment = 0
    for count in range(startCount, endCount + 1):
        interest = balance * monthlyRate
        finalInstr += interest
        monthlyPrincipal = payment - interest
        balance = balance - monthlyPrincipal
    return finalInstr, balance


def getNum(val):
    if not val:
        return 0
    else:
        return val


def amort_calc_principal(
    balance, interestRate, countingYears, terms, startCount, endCount
):
    monthlyRate = interestRate / 12
    monthlyRate = monthlyRate * 0.01
    interest = 0
    finalInstr = 0
    monthlyPrincipal = 0
    monthlyPrincipalFinal = 0
    try:
        payment = balance * (monthlyRate / (1 - math.pow(1 + monthlyRate, -terms)))
    except ZeroDivisionError:
        payment = 0
    for count in range(startCount, endCount + 1):
        interest = balance * monthlyRate
        finalInstr += interest
        monthlyPrincipal = payment - interest
        monthlyPrincipalFinal += monthlyPrincipal
        balance = balance - monthlyPrincipal
    return monthlyPrincipalFinal, balance


def amort_calc_balance(balance, interestRate, terms, startCount, endCount):
    finalInstr = 0
    monthlyRate = interestRate / 12
    monthlyRate = monthlyRate * 0.01
    interest = 0
    monthlyPrincipal = 0
    try:
        payment = balance * (monthlyRate / (1 - math.pow(1 + monthlyRate, -terms)))
    except ZeroDivisionError:
        payment = 0
    for count in range(startCount, endCount + 1):
        interest = balance * monthlyRate
        finalInstr += interest
        # calc the in-loop monthly principal and display
        monthlyPrincipal = payment - interest
        # update the balance for each loop iteration
        balance = balance - monthlyPrincipal
    return balance


def removeempty(input_list):
    xx = 0
    new_input_list = []
    for val in input_list:
        if val:
            new_input_list.append(val)
    return new_input_list


def PV(rate, nper, pmt):
    # print(rate)
    return pmt / rate * (1 - math.pow(1 + rate, -nper))


def reimbursement_calc(
    request,
    reimbursement,
    reim_ye_mo,
    reim_frequency,
    reim_increases_type,
    reim_increase_value,
    reim_increases_for_every_year,
    count,
):
    global reimbursement_income
    if reim_frequency == 0:
        if reim_increases_type == 0:
            if count == 0:
                reimbursement_income = reimbursement * 1
            elif count % reim_increases_for_every_year == 0:
                reim_increase_value = 1 + reim_increase_value * 0.01
                reimbursement_income = reimbursement_income * reim_increase_value
            else:
                reimbursement_income = reimbursement_income * 1
        else:
            if count == 0:
                reimbursement_income = reimbursement * 1
            elif count % reim_increases_for_every_year == 0:
                reimbursement_income = int(reimbursement_income) + int(
                    reim_increase_value
                )
            else:
                reimbursement_income = reimbursement_income * 1
    else:
        reim_increases_type_list = request.POST.getlist("reim_increases_type")
        reim_increase_value_list = request.POST.getlist("reim_increase_value")
        reim_increases_for_every_year_list = request.POST.getlist(
            "reim_increases_for_every_year"
        )
        for i in range(0, len(reim_increase_value_list)):
            if not reim_increase_value_list[i]:
                reim_increase_value_list[i] = 0
            actual = int(reim_increases_for_every_year_list[i]) - 1
            if int(reim_increases_type_list[i]) == 0:
                if count == 0:
                    reimbursement_income = reimbursement * 1
                elif count == actual:
                    reim_increase_value = 1 + float(reim_increase_value_list[i]) * 0.01
                    reimbursement_income = reimbursement_income * reim_increase_value
                else:
                    reimbursement_income = reimbursement_income * 1
            else:
                if count == 0:
                    reimbursement_income = reimbursement * 1
                elif count == actual:
                    reimbursement_income = int(reimbursement_income) + int(
                        reim_increase_value_list[i]
                    )
                else:
                    reimbursement_income = reimbursement_income * 1

    if reim_ye_mo == 0:
        return reimbursement_income
    else:
        return reimbursement_income * 12


def cam_calc(
    request,
    cam,
    cam_ye_mo,
    cam_frequency,
    cam_increases_type,
    cam_increase_value,
    cam_increases_for_every_year,
    count,
):
    global expense_cam
    if cam_frequency == 0:
        if cam_increases_type == 0:
            if count == 0:
                expense_cam = cam * 1
            elif count % cam_increases_for_every_year == 0:
                cam_increase_value = 1 + cam_increase_value * 0.01
                expense_cam = expense_cam * cam_increase_value
            else:
                expense_cam = expense_cam * 1
        else:
            if count == 0:
                expense_cam = cam * 1
            elif count % cam_increases_for_every_year == 0:
                expense_cam = int(expense_cam) + int(cam_increase_value)
            else:
                expense_cam = expense_cam * 1
    else:
        cam_increases_type_list = request.POST.getlist("cam_increases_type")
        cam_increase_value_list = request.POST.getlist("cam_increase_value")
        cam_increases_for_every_year_list = request.POST.getlist(
            "cam_increases_for_every_year"
        )

        for i in range(0, len(cam_increase_value_list)):
            if not cam_increase_value_list[i]:
                cam_increase_value_list[i] = 0
            actual = int(cam_increases_for_every_year_list[i]) - 1
            if int(cam_increases_type_list[i]) == 0:
                if count == 0:
                    expense_cam = cam * 1
                elif count == actual:
                    cam_increase_value = 1 + float(cam_increase_value_list[i]) * 0.01
                    expense_cam = expense_cam * cam_increase_value
                else:
                    expense_cam = expense_cam * 1
            else:
                if count == 0:
                    expense_cam = cam * 1
                elif count == actual:
                    expense_cam = int(expense_cam) + int(cam_increase_value_list[i])
                else:
                    expense_cam = expense_cam * 1

    if cam_ye_mo == 0:
        return expense_cam
    else:
        return expense_cam * 12


def utilities_calc(
    request,
    utilities,
    utilities_ye_mo,
    utilities_frequency,
    utilities_increases_type,
    utilities_increase_value,
    utilities_increases_for_every_year,
    count,
):
    global expense_utilities
    if utilities_frequency == 0:
        if utilities_increases_type == 0:
            if count == 0:
                expense_utilities = utilities * 1
            elif count % utilities_increases_for_every_year == 0:
                utilities_increase_value = 1 + utilities_increase_value * 0.01
                expense_utilities = expense_utilities * utilities_increase_value
            else:
                expense_utilities = expense_utilities * 1
        else:
            if count == 0:
                expense_utilities = utilities * 1
            elif count % utilities_increases_for_every_year == 0:
                expense_utilities = int(expense_utilities) + int(
                    utilities_increase_value
                )
            else:
                expense_utilities = expense_utilities * 1
    else:
        utilities_increases_type_list = request.POST.getlist("utilities_increases_type")
        utilities_increase_value_list = request.POST.getlist("utilities_increase_value")
        utilities_increases_for_every_year_list = request.POST.getlist(
            "utilities_increases_for_every_year"
        )

        for i in range(0, len(utilities_increase_value_list)):
            if not utilities_increase_value_list[i]:
                utilities_increase_value_list[i] = 0
            actual = int(utilities_increases_for_every_year_list[i]) - 1
            if int(utilities_increases_type_list[i]) == 0:
                if count == 0:
                    expense_utilities = utilities * 1
                elif count == actual:
                    utilities_increase_value = (
                        1 + float(utilities_increase_value_list[i]) * 0.01
                    )
                    expense_utilities = expense_utilities * utilities_increase_value
                else:
                    expense_utilities = expense_utilities * 1
            else:
                if count == 0:
                    expense_utilities = utilities * 1
                elif count == actual:
                    expense_utilities = int(expense_utilities) + int(
                        utilities_increase_value_list[i]
                    )
                else:
                    expense_utilities = expense_utilities * 1

    if utilities_ye_mo == 0:
        return expense_utilities
    else:
        return expense_utilities * 12


def management_calc(
    request,
    management,
    management_ye_mo,
    management_frequency,
    management_increases_type,
    management_increase_value,
    management_increases_for_every_year,
    count,
):
    global expense_management
    if management_frequency == 0:
        if management_increases_type == 0:
            if count == 0:
                expense_management = management * 1
            elif count % management_increases_for_every_year == 0:
                management_increase_value = 1 + management_increase_value * 0.01
                expense_management = expense_management * management_increase_value
            else:
                expense_management = expense_management * 1
        else:
            if count == 0:
                expense_management = management * 1
            elif count % management_increases_for_every_year == 0:
                expense_management = int(expense_management) + int(
                    management_increase_value
                )
            else:
                expense_management = expense_management * 1
    else:
        management_increases_type_list = request.POST.getlist(
            "management_increases_type"
        )
        management_increase_value_list = request.POST.getlist(
            "management_increase_value"
        )
        management_increases_for_every_year_list = request.POST.getlist(
            "management_increases_for_every_year"
        )

        for i in range(0, len(management_increase_value_list)):
            if not management_increase_value_list[i]:
                management_increase_value_list[i] = 0
            actual = int(management_increases_for_every_year_list[i]) - 1
            if int(management_increases_type_list[i]) == 0:
                if count == 0:
                    expense_management = management * 1
                elif count == actual:
                    management_increase_value = (
                        1 + float(management_increase_value_list[i]) * 0.01
                    )
                    expense_management = expense_management * management_increase_value
                else:
                    expense_management = expense_management * 1
            else:
                if count == 0:
                    expense_management = management * 1
                elif count == actual:
                    expense_management = int(expense_management) + int(
                        management_increase_value_list[i]
                    )
                else:
                    expense_management = expense_management * 1

    if management_ye_mo == 0:
        return expense_management
    else:
        return expense_management * 12


def administrative_calc(
    request,
    administrative,
    administrative_ye_mo,
    administrative_frequency,
    administrative_increases_type,
    administrative_increase_value,
    administrative_increases_for_every_year,
    count,
):
    global expense_administrative
    if administrative_frequency == 0:
        if administrative_increases_type == 0:
            if count == 0:
                expense_administrative = administrative * 1
            elif count % administrative_increases_for_every_year == 0:
                administrative_increase_value = 1 + administrative_increase_value * 0.01
                expense_administrative = (
                    expense_administrative * administrative_increase_value
                )
            else:
                expense_administrative = expense_administrative * 1
        else:
            if count == 0:
                expense_administrative = administrative * 1
            elif count % administrative_increases_for_every_year == 0:
                expense_administrative = int(expense_administrative) + int(
                    administrative_increase_value
                )
            else:
                expense_administrative = expense_administrative * 1
    else:
        administrative_increases_type_list = request.POST.getlist(
            "administrative_increases_type"
        )
        administrative_increase_value_list = request.POST.getlist(
            "administrative_increase_value"
        )
        administrative_increases_for_every_year_list = request.POST.getlist(
            "administrative_increases_for_every_year"
        )

        for i in range(0, len(administrative_increase_value_list)):
            if not administrative_increase_value_list[i]:
                administrative_increase_value_list[i] = 0
            actual = int(administrative_increases_for_every_year_list[i]) - 1
            if int(administrative_increases_type_list[i]) == 0:
                if count == 0:
                    expense_administrative = administrative * 1
                elif count == actual:
                    administrative_increase_value = (
                        1 + float(administrative_increase_value_list[i]) * 0.01
                    )
                    expense_administrative = (
                        expense_administrative * administrative_increase_value
                    )
                else:
                    expense_administrative = expense_administrative * 1
            else:
                if count == 0:
                    expense_administrative = administrative * 1
                elif count == actual:
                    expense_administrative = int(expense_administrative) + int(
                        administrative_increase_value_list[i]
                    )
                else:
                    expense_administrative = expense_administrative * 1

    if administrative_ye_mo == 0:
        return expense_administrative
    else:
        return expense_administrative * 12
