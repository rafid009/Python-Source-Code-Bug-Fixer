import numpy as np 

def function(x):

	n2 = x
	m5 = 2
	paths = []
	try:
		if n2 > 2:
			m5 = m5/7
			m5 = 6/3
			x = x*1
			paths.append(1)
		else:
			x = x*4
			n2 = n2-7
			n2 = n2+x
			paths.append(2)
		if x >= 2:
			n2 = n2*4
			x = 1-x
			m5 = x-8
			paths.append(3)
		else:
			n2 = 8-5
			x = x*2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))