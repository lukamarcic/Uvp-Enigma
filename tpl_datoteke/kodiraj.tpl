% rebase('tpl_datoteke\osnova.tpl')
<p>
    Izbrali ste naslednjo kodo:<br>
    Zrcalo: {{zrc}}<br>
    Rotor 1: {{rot1}}<br>
    Rotor 2: {{rot2}}<br>
    Rotor 3: {{rot3}}<br>
    Plugboard: {{pb}}<br>

    <br>
    Vneseno besedilo (urejeno, kot opisano na prejšnji strani) je: <br>
    {{tekst}}
    <br><br>

    <form action="/kodiraj/">
        <input type="submit" value="kodiraj">
    </form>

</p>