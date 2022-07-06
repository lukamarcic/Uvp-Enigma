% rebase('osnova.tpl')
<p> 
    Pozdravljeni v program "Enigma".<br>
    V programu lahko prostovoljno kodirate besedilo, kot bi to storil slaven stroj iz 2. svetovne vojne.<br>
    Če želite besedilo dekodirati, ga morate le ponovno kodirati z istimi nastavitvami za kodo.<br>
    <br>
    Kaj bi zeleli storiti?<br>
    (a): Kodirati/dekodirati besedilo<br>
    (b): Zanima me, kako deluje enigma<br>
    <br>

    <form action="/izberi/">
        <input type="submit" value="a">
        <input type="button" onclick="alert('{{sporocilo}}')" value="b">
    </form>


</p>