import numpy as np 

def function(x):

	m2 = 9
	f0 = x
	paths = []
	try:
		if m2 < 1:
			x = x+7
			m2 = m2+6
			x = f0-x
			paths.append(1)
		else:
			m2 = f0/x
			paths.append(2)
		if f0 > 9:
			m2 = 3*m2
			f0 = f0/8
			paths.append(3)
		else:
			m2 = x+5
			f0 = f0*7
			x = x/6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))