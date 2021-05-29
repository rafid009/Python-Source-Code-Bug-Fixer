import numpy as np 

def function(x):

	m0 = 6
	f2 = x
	paths = []
	try:
		if f2 <= 4:
			x = x+2
			m0 = m0*2
			m0 = m0/3
			paths.append(1)
		else:
			m0 = m0/f2
			x = x+x
			m0 = f2*9
			paths.append(2)
		if f2 < 0:
			f2 = x/f2
			x = x/5
			f2 = f2*0
			paths.append(3)
		else:
			x = x/2
			x = x*1
			m0 = 0+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))