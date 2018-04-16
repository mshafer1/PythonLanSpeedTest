#!/usr/bin/env python2

import socket
import sys
from timeit import default_timer as timer
import math
import os.path

message = '''\
Lorem ipsum dolor sit amet, invidunt accusamus no mei. Eam an errem consetetur elaboraret, ei nulla corpora tacimates sit, eum no graeco persecuti. Usu aperiri salutandi cu, ea expetenda accommodare nam. Has utinam feugiat nostrum et, vel te assum labore. Te mundi semper mei, id debet apeirian eam.

Pri dicant ullamcorper no, in mea quot quas graecis. Usu consul numquam at, amet paulo pri eu, id facete minimum contentiones sea. Utroque recteque at mea, eos magna aperiam veritus ei. Ex tollit explicari vix. Nam no vero impedit oportere.

Offendit lucilius vim eu. Ea cum partem commodo complectitur. Eum ea vidit ignota sanctus. Cu discere interesset eum, ne nam audiam rationibus.

Ne mazim quidam theophrastus his. Clita tibique accommodare ei has, has in elit libris. Te civibus principes appellantur vix. Sed no quodsi rationibus, et mea oportere evertitur. Sed no vocent senserit voluptatum.

Ex nec suas epicuri qualisque, elit harum erroribus et pro. Pri salutandi euripidis ea, ne has inani dolore debitis. Probo vivendo usu ut, ei nec perfecto singulis. Vivendo insolens mnesarchum in duo, ut euripidis dissentiunt theophrastus vix. Labitur volutpat reprehendunt ad nam, tation noster eos an. Sed oratio disputationi te, ut sed audiam regione.

Tollit dolorum dolores at nam, eu nam tation doctus euismod, usu no nemore pericula euripidis. Vero verear ponderum ex pro. Ne putent impetus rationibus pri, wisi labore an mei, discere delectus abhorreant ad his. Cum te eligendi dissentiunt. Solet doming ne qui, quas epicuri constituto ad sed.

In est possim lobortis, pri postea vulputate no, cu nostrum perpetua usu. Eu usu tempor mucius theophrastus. Ut nonumy soleat ius. Eius denique mel ei, at sit putent utroque argumentum. Ad has fierent facilisis, sit eu vivendum repudiare. Ne illud quando percipit cum.

Sonet dissentias quaerendum qui et, his in quod democritum, alia integre detraxit te sed. Nisl ceteros neglegentur te his, ad habeo legere est, utamur admodum his ex. Ut usu insolens maluisset adversarium, per et quot modus numquam. Mei et evertitur sententiae, nec virtute atomorum vituperata et, solet tincidunt sit cu.

An mei oratio dictas, modo regione laboramus mel et. Sale definiebas has eu. Ullum quando perpetua ne quo. Ex prompta explicari necessitatibus eos, sint fierent per no, mei saepe conclusionemque et.

Dolor ridens consectetuer pri no, vel ne choro alterum verterem, an tollit soluta per. Meliore inimicus petentium id mea, ius eu laudem offendit evertitur. Cu has placerat hendrerit intellegam. Eum et tempor vidisse nonumes, vis eu fugit lucilius mnesarchum. Alii primis feugait est id, unum liber salutatus nec in.

Sit ea omittam perpetua maluisset, eos ea erant ignota. Agam nominati assentior sea te, his no veri vidisse recusabo. Sale adipisci nam ne, ullum discere pro in. At sit meis maiestatis suscipiantur. His an quod idque accommodare, option disputationi ea eam. His ad omnesque salutandi, vis at dicunt ocurreret rationibus.

Sea te fierent argumentum. Suas numquam quo an, ridens causae mel ne. Ex eos probatus accusamus. Nam solum errem ne. Eu mei decore integre numquam, sed simul fuisset in, usu ei meis aperiri fabulas.

Nam ad latine intellegam. Nec ex dolorem mediocrem ullamcorper. Aeterno invidunt te per. Ut sea integre offendit, sit ad nusquam adipiscing vituperatoribus, usu errem nobis fastidii at.

Recusabo praesent eos ea, saepe utamur ea qui, sed quot periculis id. Omnium interpretaris ea duo, mel dicit offendit corrumpit ea, epicuri intellegam id his. At qui utroque percipit, nec cu duis vocibus. Ei modo falli laudem mel.

Fierent reprehendunt ex sea, pri at homero corrumpit, sed ei agam tamquam conclusionemque. Ad usu error legere quaestio. Sea quis fastidii electram ut. Simul nihil adversarium cum ne.

Meliore eloquentiam ex quo, cu errem vivendum eam. Ea sed torquatos gloriatur comprehensam. No laudem disputationi his, eu ipsum ponderum nominati eos. Consul commodo oporteat id has. Tota semper lobortis pri ut, cum agam porro forensibus no.

Usu ut suas iudicabit. Vis at nusquam pertinacia, hinc menandri gubergren nam ne. Labore propriae adversarium sea cu, cu eum graeci adipiscing. Vidisse delicatissimi ea mel, vix an fabulas vivendum aliquando. Ei reque platonem usu, periculis intellegat mea an.

Case tamquam ex quo, melius electram id est. In quot mediocrem inciderint vis, tritani probatus has ei. Ut quo maiorum expetenda. In error torquatos assueverit vim. Sed atqui nihil omnesque et.

Ad feugiat sanctus sit, perpetua gloriatur eu vis. No quot intellegat mei, id sed facilisi singulis moderatius. Est oporteat hendrerit cotidieque no, iusto sonet usu in, ut eum prodesset mediocritatem. Ei eam ceteros reformidans, ne nec scaevola antiopam, pro inani expetenda efficiendi at.

Laoreet periculis sit te, errem deserunt forensibus ius ei, autem reque per ut. Ad est placerat inciderint, in porro prodesset mei. Ad erant clita sanctus nam, ius ad liber elaboraret, dicant eleifend vel ei. Ipsum epicurei delicata ea vim. Nominavi deserunt ei his. Rebum autem qualisque in nec, civibus splendide similique ut has.
'''
server_port = 10000
server_port = 2018

unit_list = ['', 'K', 'M', 'G']

def ping(sock, message):
    # Send data
    print >>sys.stderr, 'sending '
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    received = ''
    
    while amount_received < amount_expected:
        data = sock.recv(255)
        received += data
        amount_received += len(data)
    # print >>sys.stderr, 'received:\t"%s"' % received

def client(server, string):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    
        
    server_address = (server, server_port)
    print >>sys.stderr, 'connecting to server "%s" on port: %s' % server_address
    sock.connect(server_address)

    try:
        data_size = len(string) * 8 # char to bits
        log = int(math.log(data_size, 1000))
        # print log
        data_unit = unit_list[log]
        data_size_scaled = data_size if log == 0 else data_size / (1000 ** log)
        # print data_size_scaled
        start = timer()
        ping(sock, string)
        end = timer()
        time = (end - start) / 2 # in seconds??
        
        speed=data_size/time
        log = int(math.log(speed, 1000))
        unit = unit_list[log]
        speed_scaled = speed if log == 0 else speed / (1000 ** log)
        
        highSpeed = (data_size / 8) / time
        log = int(math.log(highSpeed, 1000))
        high_unit = unit_list[log]
        highSpeed_scaled = highSpeed if log == 0 else highSpeed / (1000 ** log)
        
        # print time
        print "Sent and received {data_size_scaled} {data_unit}bits of data in {time2:.4f} seconds.".format(time2=time*2, **locals())
        print "{speed_scaled:.2f} {unit}bps or {highSpeed_scaled:.2f} {high_unit}Bps".format(**locals())

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
    

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local IP address by connecting to Google
    server_address = 'localhost'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80)) # connect
        server_address = s.getsockname()[0]
    except:
        pass
    
    # Bind the socket to the port
    server_address = (server_address, server_port)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    try:
        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(255)
                    print >>sys.stderr, 'received "%s"' % data
                    if data:
                        print >>sys.stderr, 'sending data back to the client'
                        connection.sendall(data)
                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break
                        
                    if data.strip() == 'QUIT':
                        raise Exception("Time to close")
            finally:
                # Clean up the connection
                connection.close()
    except Exception as e:
        print >>sys.stderr, 'Closing socket'
        sock.close()
        raise


if __name__ == '__main__':
    #provide for usage statement
    if len(sys.argv) > 1 and sys.argv[1] in ['/?', '-help', '--help']:
        print """Usage: {0} [server IP] [message]
  If server is not specified, {0} will open a port to act as the server"
  If message is not specified, a portion of 'Lorem Ipsum' is used""".format(os.path.basename(sys.argv[0]))
        sys.exit(0)

    # if server is provided:
    #  run client
    server_address = 'localhost'
    if len(sys.argv) > 1:
        server_address = sys.argv[1]
        if len(sys.argv) > 2:
            message = sys.argv[2]
        client(server_address, message)
    else: # start server
       server()