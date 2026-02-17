// JS fundamentals, 2.1:
//first one
<!DOCTYPE html>
<html>
<body>
  <script>
    alert( "I'm JavaScript!" );
  </script>
</body>
</html>

//second one
<!DOCTYPE html>
<html>
<body>
  <script src="alert.js"></script>
</body>
</html>

//2.4:Variaables:
//first one
let admin, name; ]
name = "John";
admin = name;
alert( admin );

//second one
const birthday = '18.04.1982';
const age = someCode(birthday);

//third one
const BIRTHDAY = '18.04.1982';
const AGE = someCode(BIRTHDAY);

//Data types:
let name = "Ilya";

// the expression is a number 1
alert( `hello ${1}` ); // hello 1

// the expression is a string "name"
alert( `hello ${"name"}` ); // hello name

// the expression is a variable, embed it
alert( `hello ${name}` );
