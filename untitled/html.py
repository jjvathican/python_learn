f = open('E:\HTML\helloworld.html','w')

message = """<!DOCTYPE html>
<html>
<head>
<head>
<link rel="stylesheet" href="styles.css">
</head>
<title>HTML Tables</title>
</head>
<body>
<table border="1">
<tr>
<td>Row 1, Column 1</td>
<td>Row 1, Column 2</td>
</tr>
<tr>
<td>Row 2, Column 1</td>
<td>Row 2, Column 2</td>
</tr>
</table>
</body>
</html>"""

f.write(message)
f.close()