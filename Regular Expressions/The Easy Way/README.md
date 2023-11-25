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
<p>Except for the control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match
themselves. You can escape a control character by preceding it with a backslash</p>
<table>
<th>
<td>Pattern</td>
<td>Description</td>
</th>
<tbody>
<tr>
<td>^</td>
<td>Matches beginning of line.</td>
</tr>
<tr>
<td>$</td>
<td>Matches end of line.</td>
</tr>
<tr>
<td>.</td>
<td>Matches any single character except newline. Using m option
allows it to match newline as well.</td>
</tr>
<tr>
<td>[...]</td>
<td>Matches any single character in brackets.</td>
</tr>
<tr>
<td>[^...]</td>
<td>Matches any single character not in brackets</td>
</tr>
<tr>
<td>re*</td>
<td>Matches 0 or more occurrences of preceding expression.</td>
</tr>
<tr>
<td>re+</td>
<td>Matches 1 or more occurrence of preceding expression.</td>
</tr>
<tr>
<td>re?</td>
<td>Matches 0 or 1 occurrence of preceding expression.</td>
</tr>
<tr>
<td>re{ n}</td>
<td>Matches exactly
expression.</td>
</tr>
<tr>
<td>re{ n,}</td>
<td>Matches n or more occurrences of preceding expression.</td>
</tr>
<tr>
<td>re{ n, m}</td>
<td>Matches at least n and at most m occurrences of preceding
expression.</td>
</tr>
<tr>
<td>a| b</td>
<td>Matches either a or b.</td>
</tr>
<tr>
<td>(re)</td>
<td>Groups regular expressions and remembers matched text.</td>
</tr>
<tr>
<td>(?imx)</td>
<td>Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.</td>
</tr>
<tr>
<td>(?-imx)</td>
<td>Temporarily toggles off i, m, or x options within a regular
expression. If in parentheses, only that area is affected.</td>
</tr>
<tr>
<td>(?: re)</td>
<td>Groups regular expressions without remembering matched text.</td>
</tr>
<tr>
<td>(?imx: re)</td>
<td>Temporarily toggles on i, m, or x options within parentheses.</td>
</tr>
<tr>
<td>(?-imx: re)</td>
<td>Temporarily toggles off i, m, or x options within parentheses.</td>
</tr>
<tr>
<td>(?#...)</td>
<td>Comment.</td>
</tr>
<tr>
<td>(?= re)</td>
<td>Specifies position using a pattern. Does not have a range.</td>
</tr>
<tr>
<td>(?! re)</td>
<td>Specifies position using pattern negation. Does not have a range.</td>
</tr>
<tr>
<td>(?> re)</td>
<td>Matches independent pattern without backtracking.</td>
</tr>
<tr>
<td>\w</td>
<td>Matches word characters.</td>
</tr>
<tr>
<td>\W</td>
<td>Matches nonword characters.</td>
</tr>
<tr>
<td>\s</td>
<td>Matches whitespace character. Equivalent to [\t\n\r\f].</td>
</tr>
<tr>
<td>\S</td>
<td>Matches nonwhitespace.[^ \t\r\n\f]</td>
</tr>
<tr>
<td>\d</td>
<td>Matches digits. Equivalent to [0-9].</td>
</tr>
<tr>
<td>\D</td>
<td>Matches nondigits.</td>
</tr>
<tr>
<td>\A</td>
<td>Matches beginning of string.</td>
</tr>
<tr>
<td>\Z</td>
<td>Matches end of string. If a newline exists, it matches just before
newline.</td>
</tr>
<tr>
<td>\z</td>
<td>Matches end of string.</td>
</tr>
<tr>
<td>\G</td>
<td>Matches point where last match finished.</td>
</tr>
<tr>
<td>\b</td>
<td>Matches word boundaries when outside brackets. Matches
backspace (0x08) when inside brackets.</td>
</tr>
<tr>
<td>\B</td>
<td>Matches nonword boundaries.</td>
</tr>
<tr>
<td>\n, \t, etc.</td>
<td>Matches newlines, carriage returns, tabs, etc.</td>
</tr>
<tr>
<td>\1...\9</td>
<td>Matches nth grouped subexpression.</td>
</tr>
<tr>
<td>\10</td>
<td>Matches nth grouped subexpression if it matched already.
Otherwise refers to the octal representation of a character code.</td>
</tr>
</tbody>
</table>