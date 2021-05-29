import numpy as np 

def function(x):

	m3 = 8
	i0 = 7
	paths = []
	try:
		if i0 < 9:
			i0 = m3+x
			paths.append(1)
		else:
			i0 = i0+1
			x = x/x
			paths.append(2)
		if x > 1:
			i0 = 1/i0
			i0 = i0*7
			m3 = 7*3
			paths.append(3)
		else:
			i0 = i0+2
			i0 = 3*i0
			m3 = 5*m3
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		m3 = i0**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))