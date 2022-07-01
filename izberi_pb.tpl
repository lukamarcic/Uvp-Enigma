% rebase('osnova.tpl')
<p>
    <form action="/kodiraj/">
        <h2>Plugboard</h2>
        Za konec potrebujemo določiti še plugboard nastavitve. <br>
        Tudi plugboard je permutacija 26 znakov, zapisana kot seznam številk 0 - 25, 
        ki paroma zamenja črke (številke) ali pa jih pusti na miru. <br>
        Torej gre za produkt 1 - 13 disjunktnih transpozicij, drugje pa je identiteta. <br>
        Spet imamo na voljo tri opcije:<br>

            <input type="radio" id="a_pb" name="izberi_pb" value="a">
            <label for="a_pb">(a): Uporabimo v naprej nastavljen plugboard</label><br>
            <input type="radio" id="b_pb" name="izberi_pb" value="b">
            <label for="b_pb">(b): Uporabimo nov, naključno generiran plugboard</label><br>
            <input type="radio" id="c_pb" name="izberi_pb" value="c">
            <label for="c_pb">(c): Uporabimo plugboard, ki ga boste določili sami</label><br>
            Če ste izbrali (c), napišite plugboard v obliki [a<small>0</small>, ... , a<small>25</small>]:
            <input type="text" id="izbira_pb" name="pb"><br><br>
    </form>
</p>