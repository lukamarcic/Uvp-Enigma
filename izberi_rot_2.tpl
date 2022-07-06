% rebase('osnova.tpl')
<p>
    Za kodiranje potrebujemo določiti začetno pozicijo naše enigme. <br><br>
    Izbran prvi rotor je: {{rot1}}
    <br><br>
    prosim določite drugi rotor:<br>   

    <form action="/izberi_rot_2/">
                
        <input type="radio" id="a_rot1" name="izberi_rotor1" value="a">
        <label for="a_rot1">(a)</label>
        <select id="a_rot1_per" name = "a_rot1_per">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        <label for="a_rot1_per">Izberite permutacijo</label>
        </select>
        <br>
        <input type="radio" id="b_rot1" name="izberi_rotor1" value="b">
        <label for="b_rot1">(b)</label><br>
        <input type="radio" id="c_rot1" name="izberi_rotor1" value="c">
        <label for="c_rot1">(c)</label><br>
        Če ste izbrali (c), napišite rotor v obliki [a<small>0</small>, ... , a<small>25</small>]:
        <input type="text" id="izbira_rot1" name="rot1"><br>
        
        <br><br>

        <label for="rot1_poz">Izberite začetno pozicijo 1. rotorja:</label>
        <select id="rot1_poz" name="rot1_poz">
            <option value="1">0</option>
            <option value="2">1</option>
            <option value="2">2</option>
            <option value="2">3</option>
            <option value="2">4</option>
            <option value="2">5</option>
            <option value="2">6</option>
            <option value="2">7</option>
            <option value="2">8</option>
            <option value="2">9</option>
            <option value="2">10</option>
            <option value="2">11</option>
            <option value="2">12</option>
            <option value="2">13</option>
            <option value="2">14</option>
            <option value="2">15</option>
            <option value="2">16</option>
            <option value="2">17</option>
            <option value="2">18</option>
            <option value="2">19</option>
            <option value="2">20</option>
            <option value="2">21</option>
            <option value="2">22</option>
            <option value="2">23</option>
            <option value="2">24</option>
            <option value="2">25</option>
        </select>

        <br><br>
            <input type="submit" value="izberi rotor 1">
    </form>
</p>