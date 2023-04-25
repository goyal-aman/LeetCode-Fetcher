#Print Words Vertically
<p>Given a string <code>s</code>. Return all the words vertically in the same order in which they appear in <code>s</code>.<br/>
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).<br/>
Each word would be put on only one column and that in one column there will be only one word.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "HOW ARE YOU"
<strong>Output:</strong> ["HAY","ORO","WEU"]
<strong>Explanation: </strong>Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "TO BE OR NOT TO BE"
<strong>Output:</strong> ["TBONTB","OEROOE","   T"]
<strong>Explanation: </strong>Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "CONTEST IS COMING"
<strong>Output:</strong> ["CIC","OSO","N M","T I","E N","S G","T"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 200</code></li>
<li><code>s</code> contains only upper case English letters.</li>
<li>It's guaranteed that there is only one space between 2 words.</li>
</ul>
