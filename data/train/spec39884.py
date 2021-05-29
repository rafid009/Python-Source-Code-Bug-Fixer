import numpy as np 

def function(x):

	k3 = x
	m7 = 9
	paths = []
	try:
		if x < 1:
			m7 = k3*2
			m7 = 6*x
			paths.append(1)
		else:
			k3 = k3*9
			paths.append(2)
		if m7 <= 4:
			m7 = 3*7
			x = x-x
			paths.append(3)
		else:
			m7 = m7+m7
			k3 = k3-0
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))