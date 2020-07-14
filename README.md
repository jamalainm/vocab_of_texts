These functions will process a spacy nlp document, compiling lists of tuples: (word, freq).

<h1>Usage:</h1>

<p>Return a spacy nlp doc from a string; ideally this will be lowercased and without special characters.</p>
<ul>
<li><code>foo = nlp(bar)</code>
<p>Where 'bar' is the name of the spacy nlp document</p>
</ul>

<p>Generate a list based on the specific word forms</p>

<ul>
<li><code>foo = word_form_freq(bar)</code>
<p>Where 'bar' is the name of the spacy nlp document</p>
</ul>

<p>Generate a list based on the lemmata</p>

<ul>
<li><code>foo = word_form_freq(bar)</code>
<p>Where 'bar' is the name of the spacy nlp document</p>
</ul>

<p>Generate a dictionary organized by lemma, sorted by frequency including word forms

<ul>
<li><code>foo = lemma_and_form(bar)</code>
<p>Where 'bar' is the name of the spacy nlp document</p>
</ul>

<p>Return a tuple of two lists: xpos tags following ittb conventions and vocab learned so far; this queries my own database so is probably not very useful for others</p>

<ul>
<li><code>foo = get_knowledge()</code>
<p>Where 'foo' is a variable name of your choosing</p>
</ul>

<p>Return a list of lemmata after running the vocab list through stanza</p>

<ul>
<li><code>foo = get_learned_lemmata()</code>
<p>Where 'foo' is a variable name of your choosing</p>
</ul>
