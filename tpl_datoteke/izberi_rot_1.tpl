% rebase('tpl_datoteke\osnova.tpl')
<p>
    Za kodiranje potrebujemo določiti začetno pozicijo naše enigme. <br><br>
    Izbrano zrcalo je: {{zrc}}

    <h2>Rotorji</h2>
    Nadaljno moramo določiti 3 rotorje in njihove začetne pozicije.<br>
    Rotor je permutacija 26 znakov, zapisana kot seznam številk 0 - 25, 
    ki vsako črko (številko) spremeni v neko drugo številko.<br>
    Torej gre za permutacijo 26 elementov brez fiksnih točk.<br>
    Rotor lahko potem še poljubno obrnemo na eno izmed 26 pozicij (označeno z 0-25).<br>
    Za vsak rotor imamo na voljo 3 opcije:<br><br>

    (a): Uporabimo eno izmed petih v naprej določenih permutacij<br>
    (b): Uporabimo novo, naključno generirano permutacijo<br>
    (c): Uporabimo permutacijo, ki jo boste določili sami<br>
    <br>
    Poleg tega moramo vsakemu rotorju določiti še začetno pozicijo, označeno s številko od vključno 0 do vključno 25.
    <br><br>

    prosim določite prvi rotor:<br>

    <form action="/izberi_rot_1/">
        
        
        <input type="radio" id="a_rot1" name="izberi_rotor1" value="a_rot1">
        <label for="a_rot1">(a)</label>
        <select id="a_rot1_per" name = "a_rot1_per">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select>
        <br>
        <input type="radio" id="b_rot1" name="izberi_rotor1" value="b_rot1">
        <label for="b_rot1">(b)</label><br>
        <input type="radio" id="c_rot1" name="izberi_rotor1" value="c_rot1">
        <label for="c_rot1">(c)</label><br>
        Če ste izbrali (c), napišite rotor v obliki [a<small>0</small>, ... , a<small>25</small>]:
        <input type="text" id="doloci_rot1" name="doloci_rot1"><br>
        
        <br><br>

        <label for="rot1_poz">Izberite začetno pozicijo 1. rotorja:</label>
        <select id="rot1_poz" name="rot1_poz">
            <option value="1">0</option>
            <option value="2">1</option>
            <option value="3">2</option>
            <option value="4">3</option>
            <option value="5">4</option>
            <option value="6">5</option>
            <option value="7">6</option>
            <option value="8">7</option>
            <option value="9">8</option>
            <option value="10">9</option>
            <option value="11">10</option>
            <option value="12">11</option>
            <option value="13">12</option>
            <option value="14">13</option>
            <option value="15">14</option>
            <option value="16">15</option>
            <option value="17">16</option>
            <option value="18">17</option>
            <option value="19">18</option>
            <option value="20">19</option>
            <option value="21">20</option>
            <option value="22">21</option>
            <option value="23">22</option>
            <option value="24">23</option>
            <option value="25">24</option>
            <option value="26">25</option>
        </select>

        <br><br>
            <input type="submit" value="izberi rotor 1">
    </form>
</p>