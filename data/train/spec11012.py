import numpy as np 

def function(x):

	m3 = x
	j2 = 5
	paths = []
	try:
		if x >= 9:
			x = x+9
			paths.append(1)
		else:
			j2 = m3/3
			paths.append(2)
		if m3 >= 2:
			x = m3*8
			x = x*4
			x = 7*1
			paths.append(3)
		else:
			m3 = 0/2
			m3 = m3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))