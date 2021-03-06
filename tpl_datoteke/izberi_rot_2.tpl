% rebase('tpl_datoteke\osnova.tpl')
<p>
    Za kodiranje potrebujemo določiti začetno pozicijo naše enigme. <br><br>
    Izbran prvi rotor je: {{rot1}}
    <br><br>
    Prosim določite drugi rotor:<br> 
    Za rotor imamo na voljo 3 opcije:<br><br>

    (a): Uporabimo eno izmed petih v naprej določenih permutacij<br>
    (b): Uporabimo novo, naključno generirano permutacijo<br>
    (c): Uporabimo permutacijo, ki jo boste določili sami<br>
    <br>

    <form action="/izberi_rot_2/">
                
        <input type="radio" id="a_rot2" name="izberi_rotor2" value="a_rot2">
        <label for="a_rot2">(a)</label>
        <select id="a_rot2_per" name = "a_rot2_per">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select>
        <br>
        <input type="radio" id="b_rot2" name="izberi_rotor2" value="b_rot2">
        <label for="b_rot2">(b)</label><br>
        <input type="radio" id="c_rot2" name="izberi_rotor2" value="c_rot2">
        <label for="c_rot2">(c)</label><br>
        Če ste izbrali (c), napišite rotor v obliki [a<small>0</small>, ... , a<small>25</small>]:
        <input type="text" id="doloci_rot2" name="doloci_rot2"><br>
        
        <br><br>

        <label for="rot2_poz">Izberite začetno pozicijo 2. rotorja:</label>
        <select id="rot2_poz" name="rot2_poz">
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
            <input type="submit" value="izberi rotor 2">
    </form>
</p>