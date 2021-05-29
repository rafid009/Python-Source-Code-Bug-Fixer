import numpy as np 

def function(x):

	v9 = x
	m1 = 7
	paths = []
	try:
		if m1 > 0:
			v9 = v9/4
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if v9 < 0:
			m1 = 9*m1
			m1 = 9*m1
			paths.append(3)
		else:
			m1 = m1*0
			v9 = v9*v9
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))