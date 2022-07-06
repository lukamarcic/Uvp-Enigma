% rebase('tpl_datoteke\osnova.tpl')
<p>
    Za kodiranje potrebujemo določiti začetno pozicijo naše enigme. <br><br>

    <form action="/izberi_zrc/">
        <h2>Zrcalo</h2>
        Najprej določimo t.i. "zrcalo": <br>
        Zrcalo je permutacija 26 znakov, zapisana kot seznam številk 0 - 25, ki paroma zamenja črke (številke). <br>
        Vresnici gre za produkt 13 disjunktnih transpozicij<br>
        Na voljo imamo tri opcije:<br>

            <input type="radio" id="a_zrc" name="izberi_zrcalo" value="a_zrc">
            <label for="a_zrc">(a): Uporabimo v naprej nastavljeno zrcalo</label><br>
            <input type="radio" id="b_zrc" name="izberi_zrcalo" value="b_zrc">
            <label for="b_zrc">(b): Uporabimo novo, naključno generirano zrcalo</label><br>
            <input type="radio" id="c_zrc" name="izberi_zrcalo" value="c_zrc">
            <label for="c_zrc">(c): Uporabimo zrcalo, ki ga boste določili sami</label><br>
            Če ste izbrali (c), napišite zrcalo v obliki [a<small>0</small>, ... , a<small>25</small>]:
            <input type="text" id="doloci_zrc" name="doloci_zrc"><br><br>

        <input type="submit" value="izberi zrcalo">
    </form>
</p>