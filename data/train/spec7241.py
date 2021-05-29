import numpy as np 

def function(x):

	m5 = x
	f3 = x
	paths = []
	try:
		if m5 >= 2:
			f3 = 3+f3
			paths.append(1)
		else:
			f3 = x+2
			m5 = m5*x
			m5 = 0/m5
			paths.append(2)
		if x >= 9:
			m5 = 6*f3
			x = f3/x
			f3 = f3*0
			paths.append(3)
		else:
			m5 = 2-m5
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))