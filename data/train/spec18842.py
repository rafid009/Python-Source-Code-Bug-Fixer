import numpy as np 

def function(x):

	f1 = 8
	m4 = x
	paths = []
	try:
		if x <= 3:
			m4 = 6*0
			m4 = 0*m4
			f1 = f1-m4
			paths.append(1)
		else:
			x = f1+f1
			paths.append(2)
		if x <= 6:
			f1 = 6/f1
			m4 = 4/9
			f1 = f1*3
			paths.append(3)
		else:
			f1 = 0+2
			m4 = x+m4
			f1 = 2+f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))