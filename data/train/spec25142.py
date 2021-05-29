import numpy as np 

def function(x):

	i4 = x
	m3 = x
	paths = []
	try:
		if i4 < 4:
			i4 = 6/i4
			m3 = 1+9
			i4 = i4+x
			paths.append(1)
		else:
			i4 = i4/6
			i4 = i4+7
			paths.append(2)
		if m3 <= 9:
			m3 = 8+m3
			x = x/1
			paths.append(3)
		else:
			m3 = m3-5
			i4 = 4*i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))