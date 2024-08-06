function validatelogin(e){
    let unameLogin = document.querySelector('#ulogin_name').value
    let passLogin = document.querySelector('#passLogin').value

    let error = false
    if(unameLogin === "" || unameLogin === null){
        document.querySelector('#unameLoginError').innerHTML="Please enter your Username"
        document.querySelector('#ulogin_name').style.border="1px solid red"
        error=true
    }else{
        document.querySelector('#unameLoginError').innerHTML=""
        document.querySelector('#ulogin_name').style.border="1px solid black"
    }
    if(passLogin === "" || passLogin === null){
        document.querySelector('#passwordLoginError').innerHTML="Please enter your Password"
        document.querySelector('#passLogin').style.border="1px solid red"
        error=true
    }else{
        document.querySelector('#passwordLoginError').innerHTML=""
        document.querySelector('#passLogin').style.border="1px solid black"
    }
    if(error){
        e.preventDefault()
    }
}


function validateregistration(e){
    // alert("Connected")
    let fname = document.querySelector('#f_name').value
    let lname = document.querySelector('#l_name').value
    let uname = document.querySelector('#u_name').value
    let email = document.querySelector('#email').value
    let password= document.querySelector('#pass').value
    let password2 = document.querySelector('#pass2').value


    let error = false
    if(fname === "" || fname === null){
        document.querySelector('#fnameError').innerHTML="Please enter your First name"
        document.querySelector('#f_name').style.border="1px solid red"
        error=true
    }else{
        document.querySelector('#fnameError').innerHTML=""
        document.querySelector('#f_name').style.border="1px solid black"
    }
    if(lname === "" || lname === null){
        document.querySelector('#lnameError').innerHTML="Please enter your Last name"
        document.querySelector('#l_name').style.border="1px solid red"
        error=true
    }else{
        document.querySelector('#lnameError').innerHTML=""
        document.querySelector('#l_name').style.border="1px solid black"
    }
    if(uname === "" || uname === null){
        document.querySelector('#unameError').innerHTML="Please enter your Username"
        document.querySelector('#u_name').style.border="1px solid red"
        error=true
    }else{
        document.querySelector('#unameError').innerHTML=""
        document.querySelector('#u_name').style.border="1px solid black"
    }


    let emailPattern = /^[a-z]+[a-z0-9\._]{3,}@[a-z]{3,10}\.[a-z\.]{2,8}$/
    if(email === "" || email === null){
        document.querySelector('#emailError').innerHTML="Please enter your Email"
        document.querySelector('#email').style.border="1px solid red"
        error=true
    }else if(!email.match(emailPattern)){
        document.querySelector('#emailError').innerHTML="Please enter a valid Email"
        document.querySelector('#email').style.border="1px solid red"
    }
    else{
        document.querySelector('#emailError').innerHTML=""
    }

    let validPassword=true
    let passError = ""
    if(!password.match(/[a-z]/)){
        passError += "\<br>Password should contain atleast one lowercase character"
        validPassword=false
    }
    if(!password.match(/[A-Z]/)){
        passError += "\<br>Password should contain atleast one uppercase character"
        validPassword=false
    }
    if(!password.match(/[0-9]/)){
        passError += "\<br>Password should contain atleast one number"
        validPassword=false
    }
    if(!password.match(/[!@#$%^&*_()]/)){
        passError += "\<br>Password should contain atleast one special character"
        validPassword=false
    }
    if(password.length < 8 || password.length > 16){
        passError += "\<br>Password must be 8-16 char long"
        validPassword=false
    }
    if(!validPassword){
        document.querySelector("#passwordError").innerHTML=passError
        document.querySelector('#pass').style.border="1px solid red"
        error=true
    }else{
        document.querySelector("#passwordError").innerHTML=""
    }
    
    if(password2 ==="" || password2 === null){
        document.querySelector("#password2Error").innerHTML="Confirm Password are required"
        document.querySelector('#pass2').style.border="1px solid red"
        error=true
    }
    else if(password != password2){
        document.querySelector("#password2Error").innerHTML="Password and Confirm Password does not match"
        document.querySelector('#pass2').style.border="1px solid red"
        error = true
    }else{
        document.querySelector("#password2Error").innerHTML=""
    }

    if(error){
        e.preventDefault()
    }
}