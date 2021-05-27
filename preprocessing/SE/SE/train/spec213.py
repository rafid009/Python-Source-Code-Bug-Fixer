import numpy as np 

def function(x):

	r8 = 7
	m9 = x
	paths = []
	try:
		if m9 > 2:
			x = 6+1
			m9 = 5*r8
			m9 = m9*m9
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x <= 0:
			r8 = m9+0
			paths.append(3)
		else:
			x = x-0
			m9 = 2*6
			r8 = 0*r8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		r8 = m9**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))