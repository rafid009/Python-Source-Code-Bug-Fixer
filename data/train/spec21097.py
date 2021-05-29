import numpy as np 

def function(x):

	j6 = 6
	m3 = x
	paths = []
	try:
		if m3 > 2:
			x = 3-8
			j6 = 4/1
			x = x*m3
			paths.append(1)
		else:
			m3 = x+m3
			j6 = 5+j6
			j6 = 1+7
			paths.append(2)
		if m3 < 7:
			x = x-0
			j6 = 5+j6
			m3 = m3*8
			paths.append(3)
		else:
			j6 = j6/8
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))