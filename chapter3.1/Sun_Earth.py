from visual import*
from math import*


def Sun_Earth(p1_vx,p1_vy,p1_vz,p2_vx,p2_vy,p2_vz):
    dt=0.002;
    p1=sphere(pos=(-100,0,0),radius=5,color=color.blue)
    p2=sphere(pos=(10,0,0),radius=10,color=color.red,material=materials.emissive)
    p1.velocity=vector(p1_vx,p1_vy,p1_vz);p2.velocity=vector(p2_vx,p2_vy,p2_vz)

   
    p1.trail=curve(color=p1.color)
    

    R=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
    GM=121*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)
    Gm=1210*(p2.velocity.x**2+p2.velocity.y**2+p2.velocity.z**2)
    
    print 'Ri=:',R
    print 'Epi=:',-GM*R**(-1)
    print 'Eki=:',0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)
    print 'Ei=:',-GM*R**(-1)+0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)
    Ei=-GM*R**(-1)+0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)

    for i in range(200000):
        rate(5000)
        R=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
        p1posxm=p1.pos.x+1/2*dt*p1.velocity.x
        p1velocityxm=p1.velocity.x+1/2*dt*(p2.pos.x-p1.pos.x)*GM*R**(-3)
        p1posym=p1.pos.y+1/2*dt*p1.velocity.y
        p1velocityym=p1.velocity.y+1/2*dt*(p2.pos.y-p1.pos.y)*GM*R**(-3)
        p1poszm=p1.pos.z+1/2*dt*p1.velocity.z
        p1velocityzm=p1.velocity.z+1/2*dt*(p2.pos.z-p1.pos.z)*GM*R**(-3)

        p2posxm=p2.pos.x+1/2*dt*p2.velocity.x
        p2velocityxm=p2.velocity.x+1/2*dt*(p1.pos.x-p2.pos.x)*Gm*R**(-3)
        p2posym=p2.pos.y+1/2*dt*p2.velocity.y
        p2velocityym=p2.velocity.y+1/2*dt*(p1.pos.y-p2.pos.y)*Gm*R**(-3)
        p2poszm=p2.pos.z+1/2*dt*p2.velocity.z
        p2velocityzm=p2.velocity.z+1/2*dt*(p1.pos.z-p2.pos.z)*Gm*R**(-3)
    
        p1.pos.x=p1.pos.x+p1velocityxm*dt
        p1.pos.y=p1.pos.y+p1velocityym*dt
        p1.pos.z=p1.pos.z+p1velocityzm*dt
        p1.velocity.x=p1.velocity.x+dt*(p2posxm-p1posxm)*GM*R**(-3)
        p1.velocity.y=p1.velocity.y+dt*(p2posym-p1posym)*GM*R**(-3)
        p1.velocity.z=p1.velocity.z+dt*(p2poszm-p1poszm)*GM*R**(-3)

        p2.pos.x=p2.pos.x+p2velocityxm*dt
        p2.pos.y=p2.pos.y+p2velocityym*dt
        p2.pos.z=p2.pos.z+p2velocityzm*dt
        p2.velocity.x=p2.velocity.x+dt*(p1posxm-p2posxm)*Gm*R**(-3)
        p2.velocity.y=p2.velocity.y+dt*(p1posym-p2posym)*Gm*R**(-3)
        p2.velocity.z=p2.velocity.z+dt*(p1poszm-p2poszm)*Gm*R**(-3)

        p1.trail.append(pos=p1.pos)
        
    
    R=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
    print 'Rf=:',R
    print 'Epf=:',-GM*R**(-1)
    print 'Ekf=:',0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)
    print 'Ef=:',-GM*R**(-1)+0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2) 
    Ef=-GM*R**(-1)+0.55*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2)
    print 'deltaE=:',Ef-Ei
    
Sun_Earth(0,-10,0,0,1,0)
