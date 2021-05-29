import numpy as np 

def function(x):

	m3 = x
	f4 = 3
	paths = []
	try:
		if m3 >= 8:
			f4 = f4-9
			x = 3/m3
			f4 = f4+2
			paths.append(1)
		else:
			x = 0/4
			x = x*3
			m3 = 8*m3
			paths.append(2)
		if m3 <= 1:
			f4 = m3-5
			f4 = 7+6
			f4 = f4-1
			paths.append(3)
		else:
			m3 = 9/m3
			f4 = f4-2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))