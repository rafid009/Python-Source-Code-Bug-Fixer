import numpy as np 

def function(x):

	f9 = x
	m6 = x
	paths = []
	try:
		if m6 >= 6:
			f9 = m6*2
			x = x*x
			paths.append(1)
		else:
			x = x*8
			x = 0*8
			paths.append(2)
		if x <= 3:
			m6 = 0+m6
			paths.append(3)
		else:
			f9 = f9+8
			f9 = f9/3
			f9 = 8*9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))