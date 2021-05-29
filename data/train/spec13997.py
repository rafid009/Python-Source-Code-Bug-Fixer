import numpy as np 

def function(x):

	i3 = 6
	m5 = 6
	paths = []
	try:
		if m5 > 4:
			m5 = m5-9
			m5 = m5*5
			x = m5*x
			paths.append(1)
		else:
			x = 9+x
			m5 = 8/m5
			m5 = 9/2
			paths.append(2)
		if m5 <= 6:
			i3 = i3-8
			x = 3*x
			i3 = x-i3
			paths.append(3)
		else:
			i3 = m5-i3
			i3 = i3-8
			x = x/2
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))