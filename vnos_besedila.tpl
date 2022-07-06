% rebase('osnova.tpl')
<p>
    Izbran plugboard je: {{pb}}<br><br>
    Za konec potrebujemo še besedilo za kodiranje.<br>
    Če želite nekaj dekodirati, je to kodirano besedilo.<br>
    <br>
    Besedilo bo enigma uredila, saj lahko kodira le znake angleške abecede.<br>
    -Šumnike bo spremenila v ustrezne črke brez strešic (torej č -> c, š -> s, ž -> z).<br>
    -Vse črke bo spremenila v male črke.<br>
    -Ostale znake (npr. đ, _, ?, !, števke 0 - 9) bo iz besedila izbrisala. Izjema so presledki, ki ostanejo.

    <form action="/izbira_besedila/">
        <input type="text" id="vnos_besedila" name="vnos_besedila" size= 1000>
        <input type="submit" value="Vnos besedila">
    </form>
</p>