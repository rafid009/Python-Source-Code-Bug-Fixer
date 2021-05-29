import numpy as np 

def function(x):

	m4 = x
	f0 = x
	paths = []
	try:
		if m4 <= 3:
			x = x+m4
			x = 0/x
			x = 4*9
			paths.append(1)
		else:
			m4 = 6+8
			f0 = x+m4
			x = x*x
			paths.append(2)
		if x < 0:
			m4 = f0-5
			paths.append(3)
		else:
			m4 = 4*m4
			m4 = f0-m4
			m4 = m4+8
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