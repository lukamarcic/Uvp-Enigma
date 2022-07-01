% rebase('osnova.tpl')
<p>
    Za kodiranje potrebujemo določiti začetno pozicijo naše enigme. <br><br>
    Izbrano zrcalo je: {{zrc}}

    <form action="/izberi_pb/">
        
        <h2>Rotorji</h2>
        Nadaljno moramo določiti 3 rotorje in njihove začetne pozicije.<br>
        Rotor je permutacija 26 znakov, zapisana kot seznam številk 0 - 25, 
        ki vsako črko(številko) spremeni v neko drugo številko.<br>
        Torej gre za permutacijo 26 elementov brez fiksnih točk.<br>
        Rotor lahko potem še poljubno obrnemo na eno izmed 26 pozicij (označeno z 0-25).<br>
        Za vsak rotor imamo na voljo 3 opcije:<br>
        <ul>
            <li>(a): Uporabimo eno izmed petih v naprej določenih permutacij</li>
            <li>(b): Uporabimo novo, naključno generirano permutacijo</li>
            <li>(c): Uporabimo permutacijo, ki jo boste določili sami</li>
        </ul>
        Poleg tega moramo vsakemu rotorju določiti še začetno pozicijo, označeno s številko od vključno 0 do vključno 25.
        <br>
        prosim določite prvi rotor:<br>

            <input type="radio" id="a_rot1" name="izberi_rotor1" value="a">
            <label for="a_rot1">(a)</label>
            <select id="a_rot1_per" name = "a_rot1_per">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            <label for="a_rot1_per">Izberite permutacijo</label>
            <br>

            <input type="radio" id="b_rot1" name="izberi_rotor1" value="b">
            <label for="b_rot1">(b)</label><br>
            <input type="radio" id="c_rot1" name="izberi_rotor1" value="c">
            <label for="c_rot1">(c)</label><br>
            Če ste izbrali (c), napišite rotor v obliki [a<small>0</small>, ... , a<small>25</small>]:
            <input type="text" id="izbira_rot1" name="rot1"><br>

            <label for="rot1_poz">Izberite začetno pozicijo 1. rotorja:</label>
            <select id="rot1_poz" name="rot1_poz">
                <option value="1">0</option>
                <option value="2">1</option>
    </form>
</p>