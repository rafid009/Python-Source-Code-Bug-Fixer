import numpy as np 

def function(x):

	k3 = x
	m7 = 2
	paths = []
	try:
		if k3 < 4:
			m7 = m7*7
			paths.append(1)
		else:
			k3 = 5/4
			x = x/m7
			m7 = k3/4
			paths.append(2)
		if x <= 2:
			x = k3*0
			k3 = k3-4
			paths.append(3)
		else:
			x = k3-k3
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