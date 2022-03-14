#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import TGate, HGate, TdgGate,SGate
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.transpiler.passes.synthesis.solovay_kitaev import SolovayKitaevDecomposition
from qiskit.quantum_info import Operator
from itertools  import tee,islice


# In[ ]:


def rz(x,circuit,qubit):
    
  
    circuit.rz(x,qubit )
    dag = circuit_to_dag(circuit)

    basis_gates = [TGate(), TdgGate(), HGate()]
    skd = SolovayKitaevDecomposition(recursion_degree=2, basis_gates=basis_gates)

    discretized = dag_to_circuit(skd.run(dag))

    pp=discretized.qasm()

    with open('ss1.qasm', 'w') as f:
        print(pp,file=f)
    def parse_qasm(qasm):
    
        lns = qasm.split(',')
        n = (lns[0])
 

    #gates = [l.split(" ") for l in lns[4:] if l]
        gates = [l.split("") for l in lns[3:] if l]
        return {'n': n, 'gates': gates, 'n_gates': len(gates)}

    def parse_qasm_file(fname,fname1):
    
        a = ['OPENQASM 2.0;','include "qelib1.inc";','qreg q[1];']
    
        with open(fname) as fin, open(fname1 , "w+") as fout:
            lines=fin.readlines()
            p=[]
            l=[]
            for i in range(4):
                p.append(lines[i::3])
        
            ll=[''.join(str(twos))+'\n' for twos in zip(*p)]

            for line in ll:
                for word in a:
                  line = line.replace(word, "1")
                line=line.replace(';',"")
                line=line.replace('q[',"")
                line=line.replace(']',"")
                line=line.replace('(',"")
                line=line.replace(')',"")
            
                line=line.replace('n',"")
                line=line.replace(',',"")
                line=line.replace("'","")
               
                line=line.replace('  \ ','  '  )
                line=line.replace('tdg','T')

                
            
                fout.write(line)


            fin.close()
            fout.close()
             #gates = [l.split(" ") for l in lns[4:] if l]
   
    
        return parse_qasm(open(fname1).read())
    gg=parse_qasm_file('ss1.qasm','ss567112390.qasm')


    print(gg)

#l=[' '.join(twos) for twos in zip(gates[::2],gates[1::2])]

    

    
def inverse_parse_file(fname1,qubit):
        

        with open(fname1+str(qubit)+'.qasm') as fin ,open(fname1+str(qubit+1)+'.qasm ','w+') as fout :

            l=fin.read().split(str(qubit)+' ')
            for line in l:

                fout.write(line+str(qubit)+' '+'\n')


            
        
            fin.close()
            fout.close()
            
        
        qc=QuantumCircuit(2)
        with open(fname1+str(qubit+1)+'.qasm') as fin:
            l=fin.readlines()
            count=0
       
            for line in l:
            
                if 'cx' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'c' and line[i]!='x' and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.cx(int(ll[0]),int(ll[1]))
                    count=count+1
                if 'T' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'h' and line[i]!= 't' and  line[i]!= 'T'  and line[i]!= ' ' and line[i]!= '\n':
                            ll.append(line[i] )
                    qc.tdg(int(ll[0]))
                    count=count+1
                if 't' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'h' and line[i]!= 't' and  line[i]!= 'T'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.t(int(ll[0]))
                    count=count+1
                if 'h' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'h' and line[i]!= 't' and  line[i]!= 'T'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.h(int(ll[0]))
                    count=count+1

                if 'ccx'  in line:
                    ll=[]
                    for i in range(len(line)):
                        if line[i] !='c'   and line[i] !='x' and  line[i] != ' ' and line[i] != '\n':
                            ll.append(line[i])
                    
                    ccx(int(ll[0]),int(ll[1]),int(ll[2]),qc)   
        print( qc.draw())

gh=inverse_parse_file('ss56711239',0)


# In[ ]:


def ccx(ii,j,k,qc):
    
    qc.h(k)
    qc.cx(j,k)
    qc.tdg(k)
    qc.cx(ii,k)
    qc.t(k)
    qc.cx(ii,j)
    qc.tdg(k)
    qc.cx(ii,k)
    qc.t(ii)
    qc.t(k)
    qc.cx(ii,j)
    qc.h(k)
    qc.t(ii)
    qc.tdg(j)
    qc.cx(ii,j)
    pppp=qc.qasm()
    with open('ss1.qasm', 'w') as f:
        print(pppp,file=f)




    def parse_qasm(qasm):
        lns = qasm.split(',')
        n = (lns[0])
    
        gates = [l.split("") for l in lns[3:] if l]
    

        return {'n': n, 'gates': gates, 'n_gates': len(gates)}

    def parse_qasm_file(fname,fname1):
    
        a = ['OPENQASM 2.0;','include "qelib1.inc";','qreg q[1];']
    
        with open(fname) as fin, open(fname1 , "w+") as fout:
            lines=fin.readlines()
            p=[]
            l=[]
            for i in range(4):
                p.append(lines[i::4])
        
            ll=[''.join(str(twos))+'\n' for twos in zip(*p)]


            for line in ll:
                for word in a:
                  line = line.replace(word, "1")
                line=line.replace(';',"")
                line=line.replace('q[',"")
                line=line.replace(']',"")
                line=line.replace('(',"")
                line=line.replace(')',"")
            
                line=line.replace('n',"")
                line=line.replace(',',"")
                line=line.replace("'","")
            #line=line.replace(" 0\ "," ")
            #line=line.replace(" 0"," ")
                line=line.replace('\ ','  ' )
                line=line.replace('tdg','T')

            #line=line.replace('tdg tdg','sdg')
            
            
            

        
            
            
                fout.write(line)


            fin.close()
            fout.close()
        return parse_qasm(open(fname1).read())
    





    

            
    gg=parse_qasm_file('ss1.qasm','ss56711230.qasm')


    print(gg)

#l=[' '.join(twos) for twos in zip(gates[::2],gates[1::2])]

    

    gh=inverse_parse_file('ss5671123')



    print(gh)
    


# In[ ]:


import numpy as np
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import TGate, HGate, TdgGate,SGate
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.transpiler.passes.synthesis.solovay_kitaev import SolovayKitaevDecomposition
from qiskit.quantum_info import Operator
from itertools  import tee,islice

circuit = QuantumCircuit(1)
circuit.rz(np.pi/5,0 )
dag = circuit_to_dag(circuit)

print('Original circuit:')
print(circuit.draw())

basis_gates = [TGate(), TdgGate(), HGate()]
skd = SolovayKitaevDecomposition(recursion_degree=2, basis_gates=basis_gates)

discretized = dag_to_circuit(skd.run(dag))





qc = QuantumCircuit(3)
qc.h(0)
qc.y(1)
qc.h(2)
qc.cx(0,1)
qc.ccx(0,1,2)
qc.z(1)
qc.rz(np.pi/5,2)

pppp=qc.qasm()


#print('Discretized circuit:')
##print(discretized.draw())

#print('Error:', np.linalg.norm(Operator(circuit).data - Operator(discretized).data))


with open('ss1.qasm', 'w') as f:
    print(pppp,file=f)




def parse_qasm(qasm):
    """Parse qasm from a string.
    """
    lns = qasm.split(',')
    n = (lns[0])
 

    #gates = [l.split(" ") for l in lns[4:] if l]
    
    gates = [l.split("") for l in lns[3:] if l]
    

    return {'n': n, 'gates': gates, 'n_gates': len(gates)}

def parse_qasm_file(fname,fname1):
    
    a = ['OPENQASM 2.0;','include "qelib1.inc";','qreg q[1];']
    
    with open(fname) as fin, open(fname1 , "w+") as fout:
        lines=fin.readlines()
        p=[]
        l=[]
        for i in range(4):
            p.append(lines[i::4])
        
        ll=[''.join(str(twos))+'\n' for twos in zip(*p)]


        for line in ll:
            for word in a:
               line = line.replace(word, "1")
            line=line.replace(';',"")
            line=line.replace('q[',"")
            line=line.replace(']',"")
            line=line.replace('(',"")
            line=line.replace(')',"")
            
            line=line.replace('n',"")
            line=line.replace(',',"")
            line=line.replace("'","")
            #line=line.replace(" 0\ "," ")
            #line=line.replace(" 0"," ")
            line=line.replace('\ ','  ' )
            #line=line.replace('tdg','T')

            #line=line.replace('tdg tdg','sdg')
            
            
            

        
            
            
            fout.write(line)


        fin.close()
        fout.close()
             #gates = [l.split(" ") for l in lns[4:] if l]
   
    """Parse a qasm file.
    """
    return parse_qasm(open(fname1).read())
    





    

            
gg=parse_qasm_file('ss1.qasm','ss567112380.qasm')


print(gg)

#l=[' '.join(twos) for twos in zip(gates[::2],gates[1::2])]
def inverse_parse_file(fname1):
        for i in range(10):

            with open(fname1+str(i)+'.qasm') as fin ,open(fname1+str(i+1)+'.qasm ','w+') as fout :

                l=fin.read().split(str(i)+' ')
                for line in l:

                    fout.write(line+str(i)+' '+'\n')


            
        
                fin.close()
                fout.close()
            
        
        qc=QuantumCircuit(3)
        with open(fname1+str(10)+'.qasm') as fin:
            l=fin.readlines()
            count=0
       
            for line in l:
            
                if 'cx' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'c' and line[i]!='x' and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.cx(int(ll[0]),int(ll[1]))
                    count=count+1
                if 'T' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'T'  and line[i]!= ' ' and line[i]!= '\n':
                            ll.append(line[i] )
                    qc.tdg(int(ll[0]))
                    count=count+1
                if 't' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 't'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.t(int(ll[0]))
                    count=count+1
                if 'h' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'h'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.h(int(ll[0]))
                    count=count+1

                if 'ccx'  in line:
                    ll=[]
                    for i in range(len(line)):
                        if line[i] !='c'   and line[i] !='x' and  line[i] != ' ' and line[i] != '\n':
                            ll.append(line[i])
                    
                    ccx(int(ll[0]),int(ll[1]),int(ll[2]),qc)   
        return  qc.draw()
    

                    
    

gh=inverse_parse_file('ss56711238')



print(gh)


# In[ ]:


def cost(fname):
    for i in range(10):
        with open(fname+str(i)+'.qasm') as fin ,open(fname+str(i+1)+'.qasm ','w+') as fout :
            l=fin.read().split(str(i)+' ')
            for line in l:
               fout.write(line+str(i)+' '+'\n')


            
        
            fin.close()
            fout.close()
        
        with open(fname+str(10)+'.qasm') as fin:
            l=fin.readlines()
            count=0
       
            for line in l:
            
                if 'cx' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'c' and line[i]!='x' and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.cx(int(ll[0]),int(ll[1]))
                    count=count+1
                if 'T' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'T'  and line[i]!= ' ' and line[i]!= '\n':
                            ll.append(line[i] )
                    qc.tdg(int(ll[0]))
                    count=count+1
                if 't' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 't'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.t(int(ll[0]))
                    count=count+1
                if 'h' in line :
                    ll=[]
                    for i in range(len(line)):
                        if line[i]!= 'h'  and line[i]!= ' ' and line[i]!= '\n':
                           ll.append(line[i] )
                    qc.h(int(ll[0]))
                    count=count+1
        return count


# In[ ]:


def checking_pattern(x,fname):
    from itertools import  permutations
    def cxhhcx(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j  in list(item)
                        line=line.replace('cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+str(j[1])+' '+ 'cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+str(j[1])+' '+'cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+ str(j[1]),'cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[0])+' '+'cx'+' '+str(j[0])+str(j[1]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    
    def cxcx2to3(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                    for item in list(perm):
                        j  = list(item)
                        line=line.replace('cx'+' '+str(j[1])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[1]),'cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[2]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def cxcxcx(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j = list(item)
                        line=line.replace('cx'+' '+str(j[1])+str(j[0])+' '+'cx'+' '+str(j[0])+str(j[2])+' '+'cx'+' '+str(j[1])+str(j[0]),'cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[1]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def cx3to2cx(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j  = list(item):
                        line=line.replace('cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[1]),'cx'+' '+str(j[0])+str(j[2])+' '+'cx'+' '+str(j[1])+str(j[2]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def cx3to3cx(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j  =list(item)
                        line=line.replace('cx'+' '+str(j[1])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[2]),'cx'+' '+str(j[0])+str(j[2])+' '+'cx'+' '+str(j[0])+str(j[1]))

                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
        
    def ticxij(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                       for j  in list(item):
                           line=line.replace('t'+' '+str(j[0])+' '+'cx'+' '+str(j[0])+str(j[1]),'cx'+' '+str(j[0])+str(j[1])+' '+'t'+' '+str(j[0]))
                           fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def hh(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                       for j  in list(item):
                           line=line.replace('h'+' '+str(j[0])+' '+'h'+" "+str(j[0]),' ')
                           fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def hxh(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                       for j  in list(item):
                           line=line.replace('h'+" "+str(j[0])+' '+ 'x'+' '+str(j[0])+' '+'h'+' '+str(j[0]),'h'+' '+str(j[0]))
                           fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def tt(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j  = list(item)
                        line=line.replace('t'+' '+str(j[0])+'t'+" "+str(j[0]),'s'+" "+str(j[0]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def TT(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j  = list(item)
                        line=line.replace('T'+' '+str(j[0])+' '+'T'+" "+str(j[0]),'S'+' '+str(j[0]))
                        fout.write()
            fin.close()
            fout.close()
        return  cost(fname2)
    def SS(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                        j= list(item)
                        line=line.replace('s'+' '+str(j[0])+' '+'s'+" "+str(j[0]),'z'+" "+str(j[0]))
                        fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
            
    def tT(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                       for j  in list(item):
                           line=line.replace('t'+' '+str(j[0])+' '+'T'+" "+str(j[0]),' ')
                           fout.write()
            fin.close()
            fout.close()
        return cost(fname2)
    def sS(fname1,fname2,num_qubits):
        p=[]
        for i in range(num_qubits):
            p.append(i)
        perm=permutations(p)

        with open(fname1) as fin, open(fname2,'w+') as fout:
            lines=fin.readlines()
            for i in range(x): 
               for line in lines:
                   for item in list(perm):
                       for j  in list(item):
                           line=line.replace('cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+str(j[1])+' '+ 'cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+str(j[1])+' '+'cx'+' '+str(j[0])+str(j[1])+' '+'h'+" "+str(j[0])+' '+'h'+' '+ str(j[1]),'cx'+' '+str(j[0])+str(j[1])+' '+'cx'+' '+str(j[1])+str(j[0])+' '+'cx'+' '+str(j[0])+str(j[1]))
                           fout.write()
            fin.close()
            fout.close()
     
        return cost(fname2)
    my_list={1:cxhhcx(),2:cxcx2to3(),3:cxcxcx(),5:ticxij(),6:cx3to2cx(),7:hh(),
    8:hxh(),9:tt(),10:TT(),11:tt(),12:SS(),13:tT(),14:sS(),15:cx3to3cx()}





     
    cost_pattern=[]
    p=[1,2,3,5,6,7,8,9,10,11,12,13,14,15]
    while (len(p)>0):
        perm=permutations(p)
        l=[]

        for item in list(perm):
            j = list(item)
            p=0
       
            for i in range(len(j)):
                pattern=my_list[j[i]]
                q=pattern(fname+str(i),fname+str(i+1))
                p=p+q
            l.append(p)
        min_index= l.index(min(l))   
        cost_pattern.append(list(perm)[min_index][0])         
        p.remove(list(perm)[min_index][0])   
             
    for i in range(len(cost_pattern)):
        pppp=my_list[cost_pattern[i]]
        pppp(fname+str(i),fname+str(i+1))
    p=inverse_parse_file(fname+str(len(cost_pattern)-1))


    return p

