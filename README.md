# Aplikacija za glasanje

pip install "uvicorn[standard]" websockets

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pip install fastapi uvicorn


<h1>Uputstvo za korišćenje aplikacije za glasanje</h1>

<h2>1. Uvod</h2>

Aplikacija omogućava administratoru da postavi pitanje sa više opcija za glasanje, dok korisnici mogu glasati sa svojih računara unutar iste mreže. Rezultati glasanja se ažuriraju u realnom vremenu.

<h2>2. API endpoints</h2>
<table>
  <tr>
    <th>Metod</th>
    <th>Endpoint</th>
    <th>Opis</th>
  </tr>
  <tr>
    <td>POST</td>
    <td> `/set_question/`</td>
    <td>Postavlja novo pitanje i opcije</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>`/cancel_question/`</td>
    <td>Briše pitanje i resetuje glasove</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>`/vote/{option}/`</td>
    <td>Glasa za izabranu opciju</td>
  </tr>
    <td>GET</td>
    <td>`/get_question/`</td>
    <td>Dohvata trenutno pitanje</td>
  <tr>
    <td>GET</td>
    <td>`/results/`</td>
    <td>Dohvata rezultate glasanja</td>
  </tr>
</table>


<h2>3. Korišćenje aplikacije</h2>

  3.1. Administrator
<li>Unosi pitanje i opcije za glasanje.</li>
<li>Klikom na "Postavi pitanje", pitanje se prosleđuje korisnicima.</li>
<li>Može videti rezultate glasanja u realnom vremenu.</li>
<li>Dugme "Cancel Question" briše trenutno pitanje i resetuje glasove. </li>
<h6>&nbsp;</h6>
  3.2. Korisnici
<li>Dobijaju pitanje i dugmad sa mogućim odgovorima.</li>
<li>Klikom na odgovor, njihov glas se čuva i prikazuje potvrda.</li>
<li>Glasovi se broje automatski i prikazuju administratoru.</li>



<h2>4. Zaključak</h2>

Ova aplikacija omogućava brzo i efikasno glasanje unutar lokalne mreže. Idealna je za anketiranje i donošenje odluka u realnom vremenu.
