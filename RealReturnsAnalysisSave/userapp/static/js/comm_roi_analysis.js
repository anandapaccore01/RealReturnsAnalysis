$(document).ready(function() {
  dynamicUpdate();
});


function dynamicUpdate(){
    var dynupdate_url = $("#ROI_data").attr("data-dynupdate-url");
    var form = $("#comm-roi-info");
    //getting tenant added numbers
    var tenant_list = $(".tenant_name");
    var tenant_nums = []
    for (var i = 0; i < tenant_list.length; i++) {
        var tenant = $(tenant_list[i]).closest('.tenant').attr('id');
        var tenant_num = tenant.match(/(\d+)/);
        tenant_nums.push(tenant_num[0]);
        console.log(tenant_nums);
    }
    form.find("#tenant_nums").remove();
    form.append('<input type="hidden" id="tenant_nums" name="tenant_nums" value="'+tenant_nums+'" /> ');
    //getting additional income added numbers
    var income_name_list = $(".income_name");
    additional_income_nums = [];
    for (var i = 0; i < income_name_list.length; i++) {
        var additional = $(income_name_list[i]).closest('.additional').attr('id');
        var additional_income_num = additional.match(/(\d+)/);
        additional_income_nums.push(additional_income_num[0]);
        console.log(additional_income_nums);
    }
    form.find("#additional_income_nums").remove();
    form.append('<input type="hidden" id="additional_income_nums" name="additional_income_nums" value="'+additional_income_nums+'" /> ');
    var closing_concession = document.getElementById('closing_consessions_view').innerHTML;
    form.find("#hidden_closing_cons_view").remove();
    form.append('<input type="hidden" id="hidden_closing_cons_view" name="closing_consessions_view" value="'+closing_concession+'" /> ');
    //getting additional expenses added numbers
    var expense_head_name_list = $(".expense_head_name");
    additional_expenses_nums = [];
    for (var i=0; i<expense_head_name_list.length; i++){
        var additional1 = $(expense_head_name_list[i]).closest('.additional1').attr('id');
        var additional_expenses_num=additional1.match(/(\d+)/);
        additional_expenses_nums.push(additional_expenses_num[0]);
        console.log(additional_expenses_nums);
    }
    form.find("#additional_expenses_nums").remove();
    form.append('<input type="hidden" id="additional_expenses_nums" name="additional_expenses_nums" value="'+additional_expenses_nums+'" /> ');
    var closing_expenses = document.getElementById('closing_expenses_view').innerHTML;
    form.find("#hidden_closing_exp_view").remove();
    form.append('<input type="hidden" id="hidden_closing_exp_view" name="closing_expenses_view" value="'+closing_expenses+'" /> ');
    if($('#YearCashFlow').length){
        var YearCashFlow = document.getElementById('YearCashFlow').innerHTML;
        form.find("#inst_sum_yearcashflow").remove();
        form.append('<input type="hidden" id="inst_sum_yearcashflow" name="inst_sum_yearcashflow" value="'+YearCashFlow+'" /> ');
    }
    if($('#BM_10').length){
        var BM_10 = document.getElementById('BM_10').innerHTML;
        form.find("#inst_sum_BM_10").remove();
        form.append('<input type="hidden" id="inst_sum_BM_10" name="inst_sum_BM_10" value="'+BM_10+'" /> ');
    }
    //adding noi_value input
    var terms = parseInt(document.getElementById("no_years").value);
    if($('#noirow').length){
      var NoiRow = document.getElementById("noirow");
		  var NoiCells = NoiRow.getElementsByTagName("td");
      if (NoiCells[terms]){
        var noi_value=NoiCells[terms].innerText;
        form.find("#noi_value").remove();
        form.append('<input type="hidden" id="noi_value" name="noi_value" value="'+noi_value+'" /> ');
      }
    }
    if($('#caprow').length){
      //adding cap_value input
      var CapRow = document.getElementById("caprow");
		  var CapCells = CapRow.getElementsByTagName("td");
      if (CapCells[1]){
        var cap_value = CapCells[1].innerText;
        form.find("#cap_value").remove();
        form.append('<input type="hidden" id="cap_value" name="cap_value" value="'+cap_value+'" /> ');
      }
      //adding capf_value input
      var CapRow = document.getElementById("caprow");
		  var CapCells = CapRow.getElementsByTagName("td");
      if(CapCells[terms]){
        var capf_value = CapCells[terms].innerText;
        form.find("#capf_value").remove();
        form.append('<input type="hidden" id="capf_value" name="capf_value" value="'+capf_value+'" /> ');
      }
    }
    //adding form data string as input
    form.find("#form_data").remove();
    form.append('<input type="hidden" id="form_data" name="form_data" value="'+form.serialize()+'" /> ');
      $.ajax({
        type: 'POST',
        url: dynupdate_url,
        data:form.serialize(), 
        success: function(data){
            form.find("#form_data").remove();
            $("#amount_down_payment").val(data.dynamic_input_update.amount_down_payment);
            $("#mortgage_loan").val(data.dynamic_input_update.mortgage_loan);
            $("#noi").val(data.dynamic_input_update.noi);
            $("#cap_rate").val(data.dynamic_input_update.cap_rate);
            $("#gross_income").val(data.dynamic_input_update.gross_income); 
            $("#year1_roi").val(data.dynamic_input_update.year1_roi); 
            $("#total_roi_percentage").val(data.dynamic_input_update.total_roi_percentage); 
            $("#total_roi").val(data.dynamic_input_update.total_roi); 
            $("#Result").html(data.invest_analysis_html);
            $("#Results").html(data.invest_summary_html);
            console.log("dynamicUpdate function called") 
  }});
}




////////////Below is modified comm_custom.js of original code////////////////////////////////


$(function () {
    $("#amount_down_payment_type").change(function () {
      if ($(this).val() == "0") {
        $("#amount_down_per").show();
        $("#amount_down_doll").hide();
      } else if ($(this).val() == "1") {
        $("#amount_down_per").hide();
        $("#amount_down_doll").show();
  
        // $("#user_input_amount").hide();
      } else {
        $("#amount_down_per").hide();
        $("#amount_down_doll").hide();
      }
    });
  });
  $(function () {
      $("#rent_increases").change(function () {
        if ($(this).val() == "0") {
          $("#rent_increases_per").show();
          $("#rent_increases_doll").hide();
        } else if ($(this).val() == "1") {
          $("#rent_increases_per").hide();
          $("#rent_increases_doll").show();
        } else {
          $("#rent_increases_per").hide();
          $("#rent_increases_doll").hide();
        }
      });
    }
  
  );
  
  
  $(function () {
      $("#asset_appraisal_type").change(function () {
        if ($(this).val() == "0") {
          $("#asset_appraisal_per").show();
          $("#asset_appraisal_doll").hide();
        } else if ($(this).val() == "1") {
          $("#asset_appraisal_per").hide();
          $("#asset_appraisal_doll").show();
        } else {
          $("#asset_appraisal_per").hide();
          $("#asset_appraisal_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#sales_expense_type").change(function () {
        if ($(this).val() == "0") {
          $("#sales_expense_per").show();
          $("#sales_expense_doll").hide();
        } else if ($(this).val() == "1") {
          $("#sales_expense_per").hide();
          $("#sales_expense_doll").show();
        } else {
          $("#sales_expense_per").hide();
          $("#sales_expense_doll").hide();
        }
      });
    }
  
  );
  
  
  $(function () {
      $("#rent_increases").change(function () {
        if ($(this).val() == "0") {
          $("#rent_increases_per").show();
          $("#rent_increases_doll").hide();
        } else if ($(this).val() == "1") {
          $("#rent_increases_per").hide();
          $("#rent_increases_doll").show();
        } else {
          $("#rent_increases_per").hide();
          $("#rent_increases_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
    $("#no_units").change(function () { //alert($(this).val());
      if ($(this).val() > 1) {
        $("#no_units_tenant").show();
  
      } else {
        $("#no_units_tenant").hide();
  
      }
    });
  });
  
  $(function () {
    $('#agree_terms').click(function () {
      if ($(this).val() == 1) {
        $("#show_save_report").show();
  
      } else {
        $("#show_save_report").hide();
  
      }
    });
  });
  
  $(function () {
      $("#lease_rate_type").change(function () {
        if ($(this).val() == "0") {
          $("#lease_rate_type_per").show();
          $("#lease_rate_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#lease_rate_type_per").hide();
          $("#lease_rate_type_doll").show();
        } else {
          $("#lease_rate_type_per").hide();
          $("#lease_rate_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#income_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#income_increases_type_per").show();
          $("#income_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#income_increases_type_per").hide();
          $("#income_increases_type_doll").show();
        } else {
          $("#income_increases_type_per").hide();
          $("#income_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#expense_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#expense_increases_type_per").show();
          $("#expense_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#expense_increases_type_per").hide();
          $("#expense_increases_type_doll").show();
        } else {
          $("#expense_increases_type_per").hide();
          $("#expense_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#taxes_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#taxes_increases_type_per").show();
          $("#taxes_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#taxes_increases_type_per").hide();
          $("#taxes_increases_type_doll").show();
        } else {
          $("#taxes_increases_type_per").hide();
          $("#taxes_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#reim_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#reim_increases_type_per").show();
          $("#reim_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#reim_increases_type_per").hide();
          $("#reim_increases_type_doll").show();
        } else {
          $("#reim_increases_type_per").hide();
          $("#reim_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#insu_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#insu_increases_type_per").show();
          $("#insu_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#insu_increases_type_per").hide();
          $("#insu_increases_type_doll").show();
        } else {
          $("#insu_increases_type_per").hide();
          $("#insu_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#hoa_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#hoa_increases_type_per").show();
          $("#hoa_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#hoa_increases_type_per").hide();
          $("#hoa_increases_type_doll").show();
        } else {
          $("#hoa_increases_type_per").hide();
          $("#hoa_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#cam_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#cam_increases_type_per").show();
          $("#cam_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#cam_increases_type_per").hide();
          $("#cam_increases_type_doll").show();
        } else {
          $("#cam_increases_type_per").hide();
          $("#cam_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#utilities_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#utilities_increases_type_per").show();
          $("#utilities_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#utilities_increases_type_per").hide();
          $("#utilities_increases_type_doll").show();
        } else {
          $("#utilities_increases_type_per").hide();
          $("#utilities_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#management_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#management_increases_type_per").show();
          $("#management_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#management_increases_type_per").hide();
          $("#management_increases_type_doll").show();
        } else {
          $("#management_increases_type_per").hide();
          $("#management_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(function () {
      $("#administrative_increases_type").change(function () {
        if ($(this).val() == "0") {
          $("#administrative_increases_type_per").show();
          $("#administrative_increases_type_doll").hide();
        } else if ($(this).val() == "1") {
          $("#administrative_increases_type_per").hide();
          $("#administrative_increases_type_doll").show();
        } else {
          $("#administrative_increases_type_per").hide();
          $("#administrative_increases_type_doll").hide();
        }
      });
    }
  
  );
  
  $(document).ready(function () {
    var i = 0;
    $('#addadditionalincome').click(function () {
      i++;
      $('#addadditional_income_dynamic').append('<div class="col-12" > </br><div class="row mt-2 additional additional_rowa' + i + '"  id="rowa' + i + '" style="border-top: 1px solid #f8f9fa;"> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09"> Income Name</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Income name. You need to enter complete address" class="fa fa-info-circle"></i>       <div class="input-group">    <input  type="text"    class="form-control income_name" id="income_name"  required placeholder="Income Name"  name="income_name">   </div>   </div>      <div class="col-12 col-lg-4 col-xl-4"></br>   <label for="validationCustom09"> Income Amount</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Income Amount" class="fa fa-info-circle"></i>  <div class="input-group"><input   type="number" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"step="any"  required class="form-control income_amount" id="income_amount"  name="income_amount" placeholder="Enter Income Amount" oninput="dynamicUpdate();" >  </div> </div><div class="col-12 col-lg-4 col-xl-4"></br>  <label for="validationCustom09"> Escalation Frequency	</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Asset Appraisal Value" class="fa fa-info-circle"></i> <div class="pull-right"><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div> <div class="input-group"> <select class="form-control income_frequency" required id="income_frequency' + i + '"  onchange="additionalFrequncy(' + i + ');dynamicUpdate();"   name="income_frequency">   <option>Choose </option>  <option value="0" selected>Equal</option>   <option value="1">Random</option></select> </div> </div> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09">Increament Val</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter amount" class="fa fa-info-circle"></i> <div class="input-group"><input   type="number" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" step="any"  required class="form-control income_increase_value"  value="0" id="income_increase_value" name="income_increase_value[' + i + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control income_increases_type" required id="income_increases_type" onchange="dynamicUpdate();" name="income_increases_type[' + i + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">  </br>  <label for="validationCustom09">  <div id="randomoptiondivadditionalYear">For Every</div> <div id="randomoptiondivadditionalAt" style="display: none">At Year</div></label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title=" No. of Units" class="fa fa-info-circle"></i>  <div class="input-group"><select  class="form-control income_increases_for_every_year" required id="income_increases_for_every_year" onchange="dynamicUpdate();" name="income_increases_for_every_year[' + i + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>      <div class="input-group-append">  <div id="randomoptiondivadditional' + i + '" style="display: none"> <button type="button" name="add"  onclick="randomoptionadditional(' + i + ')" class="btn btn-success">+</button></div></div></div> </div></div></div></br> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#rowa' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 0;
    $('#addadditionalexpense').click(function () {
      i++;
      $('#additional_expense_dynamic').append('<div class="col-12" > </br><div class="row mt-2 additional1 additional1_rowe' + i + '"  id="rowe' + i + '" style="border-top: 1px solid #f8f9fa;"> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09"> Expense Name</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Expense name. You need to enter complete address" class="fa fa-info-circle"></i>       <div class="input-group">    <input  type="text"    class="form-control expense_head_name" id="expense_head_name"  required placeholder="Expense Name"  name="expense_head_name">   </div>   </div>      <div class="col-12 col-lg-4 col-xl-4"></br>   <label for="validationCustom09"> Expense Amount</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Expense Amount" class="fa fa-info-circle"></i>  <div class="input-group"><input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control expense_amount" id="expense_amount"  name="expense_amount" placeholder="Enter Expense Amount" oninput="dynamicUpdate();" >  </div> </div><div class="col-12 col-lg-4 col-xl-4"></br>  <label for="validationCustom09"> Escalation Frequency	</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Asset Appraisal Value" class="fa fa-info-circle"></i> <div class="pull-right"><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div> <div class="input-group"> <select class="form-control expense_frequency" required id="expense_frequency' + i + '"  onchange="additionalExpenseFrequncy(' + i + ');dynamicUpdate();"   name="expense_frequency">   <option>Choose </option>  <option value="0" selected>Equal</option>   <option value="1">Random</option></select> </div> </div> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09">Increament Val</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter amount" class="fa fa-info-circle"></i> <div class="input-group"><input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control expense_increase_value"  value="0" id="expense_increase_value" name="expense_increase_value[' + i + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control expense_increases_type" required id="expense_increases_type" onchange="dynamicUpdate();" name="expense_increases_type[' + i + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">  </br>  <label for="validationCustom09">  <div id="randomoptiondivadditionalYear">For Every</div> <div id="randomoptiondivadditionalAt" style="display: none">At Year</div></label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title=" No. of Units" class="fa fa-info-circle"></i>  <div class="input-group"><select  class="form-control expense_increases_for_every_year" required id="expense_increases_for_every_year" onchange="dynamicUpdate();" name="expense_increases_for_every_year[' + i + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>      <div class="input-group-append">  <div id="randomoptiondivadditionalExpense' + i + '" style="display: none"> <button type="button" name="add"  onclick="randomoptionadditionalExpense(' + i + ')" class="btn btn-success">+</button></div></div></div> </div></div></div></br> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#rowe' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  
  $(document).ready(function () {
    var i = 0;
    $('#add').click(function () {
      i++;
      $('#dynamic_field').append('<div class="col-12" > </br><div class="row mt-2 tenant tenant_rowt' + i + '"  id="rowt' + i + '" style="border-top: 1px solid #f8f9fa;"> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09"> Tenant Name</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Asset name. You need to enter complete address" class="fa fa-info-circle"></i>       <div class="input-group">    <input  type="text"    class="form-control tenant_name" id="tenant_name"  required placeholder="Tenant Name" oninput="dynamicUpdate();" name="tenant_name">   </div>   </div>      <div class="col-12 col-lg-4 col-xl-4"></br>   <label for="validationCustom09"> SFT Leased</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Purchase Price" class="fa fa-info-circle"></i>  <div class="input-group"><input   type="number" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" step="any"  required class="form-control sft_leased" id="sft_leased"  name="sft_leased" placeholder="SFT Leased" oninput="dynamicUpdate();" >  </div> </div><div class="col-12 col-lg-4 col-xl-4"> </br><label for="validationCustom09">Rate   </label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Acquired On" class="fa fa-info-circle"></i> <div class="pull-right"><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div><div class="input-group">  <input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control lease_rate" id="lease_rate"  name="lease_rate" oninput="dynamicUpdate();" placeholder="Lease Rate"> 	<div class="input-group-append"><select class="form-control lease_rate_type" required id="lease_rate_type" onchange="dynamicUpdate();" name="lease_rate_type">   <option>Choose </option> <option value="0" selected >Rate Per Sq Ft</option>  <option value="1" >Fixed Per Month</option></select> </div>  </div>   </div><div class="col-12 col-lg-4 col-xl-4"></br>  <label for="validationCustom09"> Escalation Frequency	</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Asset Appraisal Value" class="fa fa-info-circle"></i> <div class="input-group"> <select class="form-control rent_frequency" required id="rent_frequency' + i + '"  onchange="rentFrequncy(' + i + ');dynamicUpdate();"  name="rent_frequency">   <option>Choose </option>  <option value="0" selected>Equal</option>   <option value="1">Random</option></select> </div> </div> <div class="col-12 col-lg-4 col-xl-4"></br> <label for="validationCustom09">Increament Val</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Total SFT" class="fa fa-info-circle"></i> <div class="input-group"><input   type="number" step="any"  step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control rent_increase_value"  value="0" id="rent_increase_value" name="rent_increase_value[' + i + ']" placeholder="Increase Value" onchange="dynamicUpdate();"><div class="input-group-append">   <select class="form-control rent_increases" required id="rent_increases" onchange="dynamicUpdate();" name="rent_increases[' + i + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">  </br>  <label for="validationCustom09">  <div id="randomoptiondivYear">For Every</div> <div id="randomoptiondivAt" style="display: none">At Year</div></label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title=" No. of Units" class="fa fa-info-circle"></i>  <div class="input-group"><select  class="form-control rent_increases_for_every_year" required id="rent_increases_for_every_year" onchange="dynamicUpdate();" name="rent_increases_for_every_year[' + i + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>      <div class="input-group-append">  <div id="randomoptiondiv' + i + '" style="display: none"> <button type="button" name="add"  onclick="randomoption(' + i + ')" class="btn btn-success">+</button></div></div></div> </div></div></div></br> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#rowt' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#add1').click(function () {
      i++;
      $('#dynamic_field1').append('<tr id="row' + i + '"><td><input type="text" name="expense_head_name"  placeholder="Enter Expense Name" class="form-control expense_head_name" /></td>    <td>  <div class="input-group">    <div class="input-group-append"> <span class="input-group-text">$</span> </div> <input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" class="form-control expense_amount" placeholder="Enter expense amount" name="expense_amount"></td> <td> <div class="input-group"> <select class="form-control income_frequency" required id="income_frequency" onchange="dynamicUpdate();" name="income_frequency"> <option>Choose </option> <option value="0" selected >Equal</option> <option value="1" >Random</option></select></div></td> <td>  <div class="input-group"> <select class="form-control income_increases_type" required id="income_increases_type" onchange="dynamicUpdate();" name="income_increases_type"><option>Choose </option> <option value="0" selected >Percentage</option>  <option value="1" >Fixed</option>	</select> </div></td>  <td>     <div class="input-group"> <input   type="number" step="any"  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control income_increase_value"  id="income_increase_value" name="income_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-prepend"> <span class="input-group-text">%</span> </div></div></td> <td>  <div class="input-group"><select class="form-control every_year income_increases_for_every_year" required id="income_increases_for_every_year" onchange="dynamicUpdate();" name="income_increases_for_every_year">  <option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>  </div></td> <td><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></td>  </tr> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  /*  $(document).ready(function(){  
        var i=1;  
        $('#addincome').click(function(){  
             i++;  
             $('#dynamic_field2').append('  <div class="row mt-2"  id="row'+i+'"><div class="col-12 col-lg-4 col-xl-4"> </br><label for="validationCustom09">Label</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Asset name. You need to enter complete address" class="fa fa-info-circle"></i>       <div class="input-group">   <input  type="text"  class="form-control income_name"  placeholder="Enter Expense Name"  id="income_name" name="income_name"></div>  </div> <div class="col-12 col-lg-4 col-xl-4"> </br> <label for="validationCustom09"> Amount</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Purchase Price" class="fa fa-info-circle"></i><div class="input-group">    <div class="input-group-append"> <span class="input-group-text">$</span> </div> <input   type="number"  class="form-control income_amount" id="income_amount" name="income_amount" placeholder="Income Amount"  oninput="dynamicUpdate();" ></div>    </div>	<div class="col-12 col-lg-4 col-xl-4"> </br><label for="validationCustom09">Frequency </label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Acquired On" class="fa fa-info-circle"></i>  <div class="input-group"> <select class="form-control income_frequency"  id="income_frequency" oninput="dynamicUpdate();" name="income_frequency">    <option>Choose </option>  <option value="0" selected >Equal</option> <option value="1" >Random</option></select>  </div> </div> <div class="col-12 col-lg-6 col-xl-6"></br>  <label for="validationCustom09"> Amount</label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Purchase Price" class="fa fa-info-circle"></i><div class="input-group"><input   type="text"  class="form-control income_increase_value"  id="income_increase_value" name="income_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();">       <div class="input-group-append">  <select class="form-control income_increases_type"  id="income_increases_type" oninput="dynamicUpdate();" name="income_increases_type">		    <option>Choose </option> <option value="0" selected >Percentage</option>  <option value="1" >Fixed</option>	</select> </div> </div></div><div class="col-12 col-lg-6 col-xl-6"></br> <label for="validationCustom09">At Every </label> <i aria-hidden="true" data-toggle="tooltip" data-placement="top" title="Enter Acquired On" class="fa fa-info-circle"></i><div class="input-group"> <select class="form-control  income_increases_for_every_year"  id="income_increases_for_every_year" oninput="dynamicUpdate();" name="income_increases_for_every_year">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select> <div class="input-group-append"> <button type="button" name="remove" id="'+i+'" class="btn btn-sm btn-danger btn_remove">X</button></div></div> </div></div>');  
        });  
        $(document).on('click', '.btn_remove', function(){  
             var button_id = $(this).attr("id");   
             $('#row'+button_id+'').remove();  
        });  
   }); */
  
  $(document).ready(function () {
    var i = 1;
    $('#add3').click(function () {
      i++;
      $('#dynamic_field3').append('<tr id="row' + i + '"><td><input type="text" name="closing_expensename"  placeholder="Enter  Name" class="form-control weight_list" /></td>    <td>  <div class="input-group">    <div class="input-group-append"> <span class="input-group-text">$</span> </div> <input   min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  class="form-control expensesCal" placeholder="Enter amount" name="closing_expenseamount"></div></td>  <td><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></td></tr>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#add4').click(function () {
      i++;
      $('#dynamic_field4').append('<tr id="row' + i + '"><td><input type="text" name="closing_consession_name"  placeholder="Enter  Name" class="form-control weight_list" /></td>    <td>   <div class="input-group">    <div class="input-group-append"> <span class="input-group-text">$</span> </div><input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"  oninput="dynamicUpdate();" type="number" step="any"  class="form-control consessionCal" placeholder="Enter amount" name="closing_consessionamount"></div></td>  <td><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></td></tr>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#add5').click(function () {
      i++;
      $('#dynamic_field5').append('<tr id="row' + i + '"><td><select class="form-control" name="subhead"> <option value="">Select heads</option>  <option value="Taxes">Taxes</option>  <option value="Hoa">Hoa</option>	</select> <td><select class="form-control" name="repeat_every"> <option value="">Select Years</option>  <option value="1">1</option> <option value="2">2</option></select></td> <td> <select class="form-control" required id="increment_type" name="increment_type"  oninput="dynamicUpdate();">  <option>Choose </option> <option value="0" selected >Percentage</option>   <option value="1" >Fixed</option></select>   <td>   	<div class="input-group">    <div class="input-group-append"> <span class="input-group-text">$</span> </div><input   type="number" step="any"   class="form-control consessionCal" id="value_increment"  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" name="value_increment" placeholder="Enter Value"  oninput="dynamicUpdate();" ></div></td>  <td><button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></td></tr>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addtenant').click(function () {
      i++;
      $('#tenanttable').append('<div class="col-12"> <div class="row" id="row' + i + '"><div class="col-12 col-lg-4 col-xl-4">   </div> <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control rent_increase_value"  value="0" id="rent_increase_value" name="rent_increase_value" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control rent_increases" required id="rent_increases" onchange="dynamicUpdate();" name="rent_increases">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control rent_increases_for_every_year" required id="rent_increases_for_every_year" onchange="dynamicUpdate();" name="rent_increases_for_every_year">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  function randomoption_edit(obj) {
    // alert(obj);
    var i = 1;
    /* var id = $(obj).attr("id");
    var count = id.substring(id.indexOf('addtenant')+9);
    alert(count); */
    var table_no = '#rowt' + obj;
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowt' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   </div> <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input   type="number" step="any"  required class="form-control rent_increase_value"  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"value="0" id="rent_increase_value" name="rent_increase_value_edit[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control rent_increases" required id="rent_increases" onchange="dynamicUpdate();" name="rent_increases_edit[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control rent_increases_for_every_year" required id="rent_increases_for_every_year" onchange="dynamicUpdate();" name="rent_increases_for_every_year_edit[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  function randomoption(obj) {
    // alert(obj);
    var i = 1;
    /* var id = $(obj).attr("id");
    var count = id.substring(id.indexOf('addtenant')+9);
    alert(count); */
    var table_no = '#rowt' + obj;
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowt' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   </div> <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input   type="number" step="any"  required class="form-control rent_increase_value" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"  value="0" id="rent_increase_value" name="rent_increase_value[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control rent_increases" required id="rent_increases" onchange="dynamicUpdate();" name="rent_increases[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control rent_increases_for_every_year" required id="rent_increases_for_every_year" onchange="dynamicUpdate();" name="rent_increases_for_every_year[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  function randomoptionadditional_edit(obj) {
    //alert(obj);
    var i = 1;
  
    var table_no = '#rowa' + obj; //alert(table_no);
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowa' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input   min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"type="number" step="any"  required class="form-control income_increase_value"  value="0" id="income_increase_value" name="income_increase_value_edit[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control income_increases_type" required id="income_increases_type" onchange="dynamicUpdate();" name="income_increases_type_edit[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control income_increases_for_every_year" required id="income_increases_for_every_year" onchange="dynamicUpdate();" name="income_increases_for_every_year_edit[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  function randomoptionadditional(obj) {
    //alert(obj);
    var i = 1;
  
    var table_no = '#rowa' + obj; //alert(table_no);
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowa' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input   min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control income_increase_value"  value="0" id="income_increase_value" name="income_increase_value[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control income_increases_type" required id="income_increases_type" onchange="dynamicUpdate();" name="income_increases_type[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control income_increases_for_every_year" required id="income_increases_for_every_year" onchange="dynamicUpdate();" name="income_increases_for_every_year[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  function randomoptionadditionalExpense_edit(obj) {
    //alert(obj);
    var i = 1;
  
    var table_no = '#rowe' + obj; //alert(table_no);
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowe' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control expense_increase_value"  value="0" id="expense_increase_value" name="expense_increase_value_edit[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control expense_increases_type" required id="expense_increases_type" onchange="dynamicUpdate();" name="expense_increases_type_edit[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control expense_increases_for_every_year" required id="expense_increases_for_every_year" onchange="dynamicUpdate();" name="expense_increases_for_every_year_edit[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  
  function randomoptionadditionalExpense(obj) {
    //alert(obj);
    var i = 1;
  
    var table_no = '#rowe' + obj; //alert(table_no);
    i++;
    $(table_no).append('<div class="col-12"> <div class="row" id="rowe' + obj + '' + i + '"><div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control expense_increase_value"  value="0" id="expense_increase_value" name="expense_increase_value[' + obj + ']" placeholder="Increase Value" oninput="dynamicUpdate();"><div class="input-group-append">   <select class="form-control expense_increases_type" required id="expense_increases_type" onchange="dynamicUpdate();" name="expense_increases_type[' + obj + ']">   <option>Choose </option>  <option value="0" selected >Percentage</option>    <option value="1" >Fixed</option></select>    </div>         </div>        </div> 		          <div class="col-12 col-lg-4 col-xl-4">   <div class="input-group"><select  class="form-control expense_increases_for_every_year" required id="expense_increases_for_every_year" onchange="dynamicUpdate();" name="expense_increases_for_every_year[' + obj + ']">	<option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select>       <button type="button" name="remove" id="' + obj + '' + i + '" class="btn btn-sm btn-danger  btn_remove">X</button></div></div></div></div>');
  
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  }
  
  $(document).ready(function () {
    var i = 1;
    $('#addhoa').click(function () {
      i++;
      $('#hoatable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control hoa_increase_value"   id="hoa_increase_value" name="hoa_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control insu_increases_type" required id="hoa_increases_type" onchange="dynamicUpdate();" name="hoa_increases_type">     <option value="0" selected >Percentage</option>	    <option value="1" >Fixed</option>   </select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control hoa_increases_for_every_year" required id="hoa_increases_for_every_year" onchange="dynamicUpdate();" name="hoa_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div></div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  
  $(document).ready(function () {
    var i = 1;
    $('#addtaxes').click(function () {
      i++;
      $('#taxestable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control taxes_increase_value"   id="taxes_increase_value" name="taxes_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control taxes_increases_type" required id="taxes_increases_type" onchange="dynamicUpdate();" name="taxes_increases_type">      <option value="0" selected >Percentage</option>	    <option value="1" >Fixed</option>   </select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control taxes_increases_for_every_year" required id="taxes_increases_for_every_year" onchange="dynamicUpdate();" name="taxes_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div></div> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addreim').click(function () {
      i++;
      $('#reimbursementtable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control reim_increase_value"   id="reim_increase_value" name="reim_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control reim_increases_type" required id="reim_increases_type" onchange="dynamicUpdate();" name="reim_increases_type">      <option value="0" selected >Percentage</option>	      <option value="1" >Fixed</option></select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control reim_increases_for_every_year" required id="reim_increases_for_every_year" onchange="dynamicUpdate();" name="reim_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div> </div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addcam').click(function () {
      i++;
      $('#camtable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"  type="number" step="any"  required class="form-control cam_increase_value"   id="cam_increase_value" name="cam_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control cam_increases_type" required id="cam_increases_type" onchange="dynamicUpdate();" name="cam_increases_type">     <option value="0" selected >Percentage</option>	    <option value="1" >Fixed</option>   </select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control cam_increases_for_every_year" required id="cam_increases_for_every_year" onchange="dynamicUpdate();" name="cam_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div> </div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addutilities').click(function () {
      i++;
      $('#utilitiestable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"  type="number" step="any"  required class="form-control utilities_increase_value"   id="utilities_increase_value" name="utilities_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control utilities_increases_type" required id="utilities_increases_type" onchange="dynamicUpdate();" name="utilities_increases_type">     <option value="0" selected >Percentage</option>	     <option value="1" >Fixed</option></select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control utilities_increases_for_every_year" required id="utilities_increases_for_every_year" onchange="dynamicUpdate();" name="utilities_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div> </div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addmanagement').click(function () {
      i++;
      $('#managementtable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null"  required class="form-control management_increase_value"   id="management_increase_value" name="management_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control management_increases_type" required id="management_increases_type" onchange="dynamicUpdate();" name="management_increases_type">     <option value="0" selected >Percentage</option>	       <option value="1" >Fixed</option></select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control management_increases_for_every_year" required id="management_increases_for_every_year" onchange="dynamicUpdate();" name="management_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div></div> ');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addadministrative').click(function () {
      i++;
      $('#administrativetable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input   type="number" step="any" min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" required class="form-control administrative_increase_value"   id="administrative_increase_value" name="administrative_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control administrative_increases_type" required id="administrative_increases_type" onchange="dynamicUpdate();" name="administrative_increases_type">      <option value="0" selected >Percentage</option>	     <option value="1" >Fixed</option></select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control administrative_increases_for_every_year" required id="administrative_increases_for_every_year" onchange="dynamicUpdate();" name="administrative_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div> </div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  
  $(document).ready(function () {
  
    $("#dynamic_field4").on('input', '.consessionCal', function () {
      var calculated_total_sum = 0;
  
      $("#dynamic_field4 .consessionCal").each(function () {
        var get_textbox_value = $(this).val();
        if ($.isNumeric(get_textbox_value)) {
          calculated_total_sum += parseFloat(get_textbox_value);
        }
      });
      $("#closing_consessions_view").html(calculated_total_sum);
      dynamicUpdate();
    });
  
  });
  
  
  $(document).ready(function () {
  
    $("#dynamic_field3").on('input', '.expensesCal', function () {
      var calculated_total_sum = 0;
  
      $("#dynamic_field3 .expensesCal").each(function () {
        var get_textbox_value = $(this).val();
        if ($.isNumeric(get_textbox_value)) {
          calculated_total_sum += parseFloat(get_textbox_value);
        }
      });
      $("#closing_expenses_view").html(calculated_total_sum);
      dynamicUpdate();
    });
  
  });
  
  $(document).ready(function () {
    var i = 1;
    $('#addinsu').click(function () {
      i++;
      $('#insurancetable').append('<div class="col-12"><div class="row" id="row' + i + '"><div class="col-12 col-lg-6 col-xl-6" ></br><div class="input-group"> <input  min="0" onblur="this.value =!!this.value && Math.abs(this.value) >= 0 ? Math.abs(this.value) : null" type="number" step="any"  required class="form-control insu_increase_value"   id="insu_increase_value" name="insu_increase_value" placeholder="Increase Value"  oninput="dynamicUpdate();"> <div class="input-group-append">  <select class="form-control insu_increases_type" required id="insu_increases_type" onchange="dynamicUpdate();" name="insu_increases_type">     <option value="0" selected >Percentage</option>	    <option value="1" >Fixed</option>   </select>    </div> 	</div> </div>  <div class="col-12 col-lg-6 col-xl-6">	</br><div class="input-group"> <select class="form-control insu_increases_for_every_year" required id="insu_increases_for_every_year" onchange="dynamicUpdate();" name="insu_increases_for_every_year"><option value="1" selected >1 Year</option> <option value="2" >2 Year</option> <option value="3" >3 Year</option><option value="4" >4 Year</option> <option value="5" >5 Year</option><option value="6"  >6 Year</option> <option value="7" >7 Year</option> <option value="8" >8 Year</option><option value="9" >9 Year</option> <option value="10" >10 Year</option></select><div class="input-group-append">  <button type="button" name="remove" id="' + i + '" class="btn btn-sm btn-danger btn_remove">X</button></div></div></div></div></div>');
    });
    $(document).on('click', '.btn_remove', function () {
      var button_id = $(this).attr("id");
      $('#row' + button_id + '').remove();
      dynamicUpdate();
    });
  });
  
  
  $(document).ready(function () {
    $("#add_more_expenses").click(function () {
      $("#add_more_expense_form").toggle(1000);
    });
  });
  
  $(document).ready(function () {
    $("#add_more_escalations").click(function () {
      $("#add_more_escalations_form").toggle(1000);
    });
  });
  
  
  function rentFrequncy(obj) {
    //alert(obj);
    /*   var id = $(obj).attr("id");
     var count = id.substring(id.indexOf('rent_frequency')+14);
               alert(count);  */
    var divid = '#randomoptiondiv' + obj;
    var rent_frequencyid = 'rent_frequency' + obj;
  
    var val = document.getElementById(rent_frequencyid).value; //alert(val);
    if (val == 1) {
      $(divid).show();
      $("#randomoptiondivYear").hide();
      $("#randomoptiondivAt").show();
    } else {
      $(divid).hide();
      $("#randomoptiondivYear").show();
      $("#randomoptiondivAt").hide();
    }
  
  }
  
  function additionalExpenseFrequncy(obj) {
    //alert(obj);
    /*   var id = $(obj).attr("id");
     var count = id.substring(id.indexOf('rent_frequency')+14);
               alert(count);  */
    var divid = '#randomoptiondivadditionalExpense' + obj;
    var expense_frequencyid = 'expense_frequency' + obj;
  
    var val = document.getElementById(expense_frequencyid).value; //alert(val);
    if (val == 1) {
      $(divid).show();
      $("#randomoptiondivadditional_expenseYear").hide();
      $("#randomoptiondivadditional_expenseAt").show();
    } else {
      $(divid).hide();
      $("#randomoptiondivadditional_expenseYear").show();
      $("#randomoptiondivadditional_expenseAt").hide();
    }
  
  }
  
  function additionalFrequncy(obj) {
    //alert(obj);
  
    var divid = '#randomoptiondivadditional' + obj; //alert(divid);
    var additional_frequencyid = 'income_frequency' + obj;
  
    var val = document.getElementById(additional_frequencyid).value; //alert(val);
    if (val == 1) { //alert(val);
      $(divid).show();
      $("#randomoptiondivadditionalYear").hide();
      $("#randomoptiondivadditionalAt").show();
    } else {
      $(divid).hide();
      $("#randomoptiondivadditionalYear").show();
      $("#randomoptiondivadditionalAt").hide();
    }
  
  }
  
  
  /* $(function () {
  
  $(".rent_frequency").bind( "change", function() {
        //  $(".rent_frequency").change(function () { //alert($(this).val());
              
                var count = id.substring(id.indexOf('rent_frequency')+14);
                 alert(count);
              if ($(this).val() == 1) {
                  $("#randomoptiondiv"+count).show();
                  $("#randomoptiondivYear").hide();
                  $("#randomoptiondivAt").show();
              } else {
                  $("#randomoptiondiv"+count).hide();
                  $("#randomoptiondivYear").show();
                      $("#randomoptiondivAt").hide();
              }
          });
      });*/
  
  
  $(function () {
    $("#hoa_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivhoa").show();
        $("#randomoptiondivhoaYear").hide();
        $("#randomoptiondivhoaAt").show();
      } else {
        $("#randomoptiondivhoa").hide();
        $("#randomoptiondivhoaYear").show();
        $("#randomoptiondivhoaAt").hide();
      }
    });
  });
  
  $(function () {
    $("#reim_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivreim").show();
        $("#randomoptiondivreimYear").hide();
        $("#randomoptiondivreimAt").show();
      } else {
        $("#randomoptiondivreim").hide();
        $("#randomoptiondivreimYear").show();
        $("#randomoptiondivreimAt").hide();
      }
    });
  });
  
  $(function () {
    $("#cam_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivcam").show();
        $("#randomoptiondivcamYear").hide();
        $("#randomoptiondivcamAt").show();
      } else {
        $("#randomoptiondivcam").hide();
        $("#randomoptiondivcamYear").show();
        $("#randomoptiondivcamAt").hide();
      }
    });
  });
  
  $(function () {
    $("#utilities_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivutilities").show();
        $("#randomoptiondivutilitiesYear").hide();
        $("#randomoptiondivutilitiesAt").show();
      } else {
        $("#randomoptiondivutilities").hide();
        $("#randomoptiondivutilitiesYear").show();
        $("#randomoptiondivutilitiesAt").hide();
      }
    });
  });
  
  $(function () {
    $("#management_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivmanagement").show();
        $("#randomoptiondivmanagementYear").hide();
        $("#randomoptiondivmanagementAt").show();
      } else {
        $("#randomoptiondivmanagement").hide();
        $("#randomoptiondivmanagementYear").show();
        $("#randomoptiondivmanagementAt").hide();
      }
    });
  });
  
  $(function () {
    $("#administrative_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivadministrative").show();
        $("#randomoptiondivadministrativeYear").hide();
        $("#randomoptiondivadministrativeAt").show();
      } else {
        $("#randomoptiondivadministrative").hide();
        $("#randomoptiondivadministrativeYear").show();
        $("#randomoptiondivadministrativeAt").hide();
      }
    });
  });
  
  
  $(function () {
    $("#taxes_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivtaxes").show();
        $("#randomoptiondivtaxesYear").hide();
        $("#randomoptiondivtaxesAt").show();
      } else {
        $("#randomoptiondivtaxes").hide();
        $("#randomoptiondivtaxesYear").show();
        $("#randomoptiondivtaxesAt").hide();
      }
    });
  });
  
  $(function () {
    $("#insu_frequency").change(function () { //alert($(this).val());
      if ($(this).val() == 1) {
        $("#randomoptiondivinsurance").show();
        $("#randomoptiondivinsuranceYear").hide();
        $("#randomoptiondivinsuranceAt").show();
      } else {
        $("#randomoptiondivinsurance").hide();
        $("#randomoptiondivinsuranceYear").show();
        $("#randomoptiondivinsuranceAt").hide();
      }
    });
  });
  
  $(document).ready(function () {
    var $select = $(".every_year");
    var str = $('.no_years').val();
  
    for (i = 1; i <= 10; i++) {
      $select.append($('<option></option>').val(i).html(i))
    }
  });
  
  $(document).ready(function () {
    fetch_data();
    $('#butsave').on('click', function () {
      var subhead = $('#subhead').val();
      var repeat_every = $('#repeat_every').val();
      var increment_type = $('#increment_type').val();
      var value_increment = $('#value_increment').val();
  
      if (subhead != "" && repeat_every != "" && increment_type != "" && value_increment != "") {
        //   $("#butsave").attr("disabled", "disabled");
        $.ajax({
          url: "/storeEscalations",
          type: "POST",
          headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
          },
          data: {
            _token: $("#csrf").val(),
            subhead: subhead,
            repeat_every: repeat_every,
            increment_type: increment_type,
            value_increment: value_increment
          },
          cache: false,
          success: function (dataResult) {
            console.log(dataResult);
            var dataResult = JSON.parse(dataResult);
            if (dataResult.statusCode == 200) {
              //window.location = "/userData";
              fetch_data();
              // alert("Escalation Added!");					
            } else if (dataResult.statusCode == 201) {
              alert("Error occured !");
            }
  
          }
        });
      } else {
        alert('Please fill all the field !');
      }
    });
  });
  $(document).on('click', '.delete', function () {
    var id = $(this).attr("id"); // alert(id);
    if (confirm("Are you sure you want to delete this escalations?")) {
      $.ajax({
        url: "/delete_escalation_data",
        method: "POST",
        headers: {
          'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        },
        data: {
          id: id,
          _token: $("#csrf").val()
        },
        success: function (data) {
          $('#message').html(data);
          fetch_data();
        }
      });
    }
  });
  
  function fetch_data() {
    $.ajax({
      url: "/fetch_escalation_data",
      dataType: "json",
      success: function (data) {
        var html = '';
  
        for (var count = 0; count < data.length; count++) {
          html += '<tr>';
          html += '<td contenteditable class="column_name" data-column_name="subhead" data-id="' + data[count].id + '">' + data[count].subhead + '</td>';
          html += '<td contenteditable class="column_name" data-column_name="repeat_every" data-id="' + data[count].id + '">' + data[count].repeat_every + '</td>';
          html += '<td contenteditable class="column_name" data-column_name="increment_type" data-id="' + data[count].id + '">' + data[count].increment_type + '</td>';
          html += '<td contenteditable class="column_name" data-column_name="value_increment" data-id="' + data[count].id + '">' + data[count].value_increment + '</td>';
          html += '<td><button type="button" class="btn btn-danger btn-xs delete" id="' + data[count].id + '">Delete</button></td></tr>';
        }
        // $('tbody').html(html);
        $("#userTable").html(html);
      }
    });
  }
  

//////////////Validations alert script start/////////////////

$(document).ready(function () {

  $("#alert-warning").click(function (e) {
    e.preventDefault();
    if ($('#asset_name').val().trim() == '') {
      alert("Warning! Please input Asset Name");
    } else if ($('#original_purchase_price').val().trim() == '') {
      alert("Warning! Please input Purchase Price");
    } else if ($('#no_years').val().trim() == '') {
      alert("Warning! Please input Holding Period");
    } else if ($('#total_sft').val().trim() == '') {
      alert("Warning! Please input Total SFT ");
    } else if ($('#annual_rate_interests').val().trim() == '') {
      alert("Warning! Please input Annual Rate of Interest");
    } else if ($('#amount_down_payment').val().trim() == '') {
      alert("Warning! Please input Amount of Down Payment");
    } else if ($('#mortgage_loan').val().trim() == '') {
      alert("Warning! Please input Mortagage Loan");
    } else if ($('#tenant_name').val().trim() == '' || $('#sft_leased').val().trim() == '' || $('#lease_rate').val().trim() == '') {
      alert("Warning! Please input Tenant Missing Details");
    } else {
      $("#wallet").modal('show');
    }
  });
});

//////////////Validations alert script end/////////////////


//////////////Delete scripts for edit/update report start////////////

$(".deleteTenant").click(function(){ 
  var id = $(this).data("id"); 
  var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#row"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteTenant/'+arr[0], domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
    $(remove_id).remove();
    dynamicUpdate();
          // $(this).parents("row"+id).remove();
      }
  });
 
});

$(".deleteTenantEscalations").click(function(){
  var id = $(this).data("id"); 
  var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#rowET"+arr[1];
  var remove_id1 = "#rowET1"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteTenantEscalations/'+id, domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
    $(remove_id).remove();
    $(remove_id1).remove();
    dynamicUpdate();
          // $(this).parents("row"+id).remove();
      }
  });
 
});
$(".deleteExpenseEscalations").click(function(){
  var id = $(this).data("id"); 
  var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#rowEE"+arr[1];
  var remove_id1 = "#rowEE1"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteAdditionalEscalations/'+id, domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
    $(remove_id).remove();
    $(remove_id1).remove();
    dynamicUpdate();
          // $(this).parents("row"+id).remove();
      }
  });
 
});

$(".deleteIncomeEscalations").click(function(){ 
  var id = $(this).data("id"); 
  var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#rowEI"+arr[1];
  var remove_id1 = "#rowEI1"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteAdditionalEscalations/'+id, domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
    $(remove_id).remove();
    $(remove_id1).remove();
    dynamicUpdate();
          // $(this).parents("row"+id).remove();
      }
  });
 
});

$(".deleteSubheads").click(function(){ 
  var id = $(this).data("id"); //alert(id);
var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#rowa"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteSubheads/'+arr[0], domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
        $(remove_id).remove();
    dynamicUpdate();
      }
  });
 
});



$(".deleteSubheadsExpense").click(function(){ 
  var id = $(this).data("id"); //alert(id);
var arr = id.split("-");//alert (arr[0]);
  var csrftoken = $("#ROI_data").attr("data-csrf");
  var remove_id = "#rowe"+arr[1];
  var domain = $("#ROI_data").attr("data-domain");
  var del_url = new URL('analysis/deleteSubheads/'+arr[0], domain);
  $.ajax(
  {
      url: del_url,
      type: 'POST',
      data: {
          "id": id,
          "csrfmiddlewaretoken": csrftoken,
      },
      success: function (){
        $(remove_id).remove();
    dynamicUpdate();
      }
  });
 
});


//////////////Delete scripts for edit/update report end////////////