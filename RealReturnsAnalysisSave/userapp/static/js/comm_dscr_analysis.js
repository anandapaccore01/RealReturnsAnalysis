function dynamicUpdate(){
    var dynupdate_url = $("#DSCR_data").attr("data-dynupdate-url");
    var form = $("#comm-dscr-info");
    $.ajax({
        type: 'POST',
        url: dynupdate_url,
        data:form.serialize(), 
        success: function(data){
            if (data.dynamic_input_update.less_vacancy){
                document.getElementById("less_vacancy").innerHTML  = '$ '+ numberWithCommas(parseFloat(data.dynamic_input_update.less_vacancy).toFixed(0));
            }
            document.getElementById("total_annual_rents").innerHTML  = '$ '+numberWithCommas(data.dynamic_input_update.total_annual_rents);
            document.getElementById("effective_total_annual_rents").innerHTML  = '$ '+numberWithCommas(data.dynamic_input_update.effective_total_annual_rents.toFixed(0));
            document.getElementById("total_operating_expenses").innerHTML  = '$ '+numberWithCommas(data.dynamic_input_update.total_operating_expenses); 
            document.getElementById("less_reserves").innerHTML  = '$ '+numberWithCommas(data.dynamic_input_update.less_reserves);
            document.getElementById("monthly_loan_payment").innerHTML  =   '$ '+numberWithCommas(data.dynamic_input_update.monthly_loan_payment_prev);
            document.getElementById("loan_amount").value = data.dynamic_input_update.loan_amount.toFixed(0);
            document.getElementById("down_payment").value = data.dynamic_input_update.downpayment_val.toFixed(0);
	        document.getElementById("ltv").value = data.dynamic_input_update.ltv.toFixed(2);
            if (data.dynamic_input_update.down_revised){
                document.getElementById("down_payment").value =	data.dynamic_input_update.down_revised.toFixed(0);
            } 
            if (data.dynamic_input_update.floan_amount){
                document.getElementById("loan_amount").value = data.dynamic_input_update.floan_amount.toFixed(0);               
            }
            document.getElementById("annual_debt").innerHTML   = '$ '+numberWithCommas(parseFloat(data.dynamic_input_update.ADS).toFixed(0)) ;
            document.getElementById("cash_flow").innerHTML  =  '$ '+numberWithCommas(data.dynamic_input_update.cash_flow.toFixed(0));
            document.getElementById("less_annual_debt").innerHTML  = '$ '+ numberWithCommas(data.dynamic_input_update.ADS.toFixed(0));
            document.getElementById("cash_flow_after_debt_service").innerHTML = '$ '+ numberWithCommas(parseFloat(data.dynamic_input_update.cash_flow_after_debt_service).toFixed(0));
            document.getElementById("debt_service_coverage_ratio").innerHTML  = data.dynamic_input_update.debt_service_coverage_ratio.toFixed(2)+'x';
            document.getElementById("dscr_ratio").value = data.dynamic_input_update.debt_service_coverage_ratio.toFixed(2);
            
            document.getElementById("loan_amount_prev").innerHTML  =   '$ '+ numberWithCommas(document.getElementById("loan_amount").value);
            document.getElementById("downpayment_prev").innerHTML  =   '$ '+ numberWithCommas(document.getElementById("down_payment").value);
            document.getElementById("ltv_prev1").innerHTML =  data.dynamic_input_update.ltv.toFixed(2);
            console.log("dynamicUpdate function called");
  }});
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}


//////////////Validations alert script start/////////////////

$(document).ready(function () {
    $("#alert-warning").click(function (e) {
      e.preventDefault();
      if ($('#borrower_name').val().trim() == '') {
        alert("Warning! Please input Borrower Name");
      } else if ($('#property_type').val().trim() == '') {
        alert("Warning! Please Select Property Type");
      } else if ($('#no_units').val().trim() == '') {
        alert("Warning! Please select  No. of Units");
      } else if ($('#approximate_sq_footage').val().trim() == '') {
        alert("Warning! Please input Sq Footage");
      } else if ($('#property_value').val().trim() == '') {
        alert("Warning! Please input Property Value");
      } else if ($('#loan_amount').val().trim() == '') {
        alert("Warning! Please input Loan Amount in");
      } else if ($('#amortization_years').val().trim() == '') {
        alert("Warning! Please Select amortization years");
      } else if ($('#down_payment').val().trim() < 0 || $('#down_payment').val().trim() == '') {
        alert("Warning! Down payment should not be negative please adjust");
      } else if ($('#loan_amount').val().trim() < 0) {
        alert("Warning! Loan amount should not be negative please adjust");
      } else {
        $("#wallet").modal('show');
      }
    });
  });
  
  //////////////Validations alert script end/////////////////