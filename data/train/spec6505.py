import numpy as np 

def function(x):

	m9 = 4
	f8 = x
	paths = []
	try:
		if f8 <= 9:
			m9 = m9/5
			f8 = f8/2
			paths.append(1)
		else:
			f8 = m9/f8
			f8 = 5*1
			f8 = 2+f8
			paths.append(2)
		if m9 > 0:
			f8 = 8*f8
			x = x*x
			m9 = m9/8
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))