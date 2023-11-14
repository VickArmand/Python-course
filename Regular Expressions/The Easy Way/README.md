<h1>Using Regular Expressions In Python</h1>
<h4>Steps</h4>
<ul>
<li>Import the regex module with import re.</li>
<li>Create a Regex object with the re.compile() function. (Remember to use a
raw string.)</li>
<li>Pass the string you want to search into the Regex object’s search() method.</li>
This returns a Match object.
<li>Call the Match object’s group() method to return a string of the actual
matched text.</li>
</ul>