# Snake By A
This is building on some of the earlier development within the first directory. This is implemented following object-orientation but have been written over a very long period of time. Mainly the base of the gamestate gameworld and menus were written during or around my first year of studies, while I've now (early year 3) begun studying AI and will extend this project to implement different AI techniques for the snake to move around.

## Author
Albin Sidås <br>
albinsidas@gmail.com

## TODO:

1. Refreshrate hämtas inte från config

2. Kolla hur det fungerar ifall man byter storelk på mappen (boardsize)

3. Implementera ett gäng modeller att testa runt med, börja med search och sedan gå över och testa Qlearning
den sistnämnda kommer dock kräva ändringar av refreshrate etc. för träning

4. Vore nice att lösa en Hamilton-graf implementation för att garantera att alltid klara hela kartan (<br>
    hamiltongraf = besöka alla noder och bågar endast en gång <br>
    Om detta är möjligt kommer ormen följa den graphiterationen genom hela kartan och därmed förskra att <br>
    den alltid klarar uppgiften men kommer troligen ta lång tid eftersom den går genom alla noder för varje iteration och frukt.<br>

)<br>