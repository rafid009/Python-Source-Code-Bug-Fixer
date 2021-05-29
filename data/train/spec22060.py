import numpy as np 

def function(x):

	k3 = x
	m5 = 3
	x = x
	paths = []
	try:
		if k3 < 7:
			x = x*5
			k3 = 8+k3
			k3 = k3+3
			paths.append(1)
		else:
			k3 = k3*0
			m5 = 9*k3
			paths.append(2)
		if k3 < 1:
			m5 = x/9
			paths.append(3)
		else:
			x = x-m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		k3 = m5**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))