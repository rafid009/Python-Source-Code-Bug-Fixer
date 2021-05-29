import numpy as np 

def function(x):

	m2 = 6
	t2 = x
	paths = []
	try:
		if m2 > 1:
			t2 = t2-0
			x = 8*1
			x = 1-5
			paths.append(1)
		else:
			t2 = t2*0
			paths.append(2)
		if x >= 3:
			x = 1*x
			paths.append(3)
		else:
			m2 = x/1
			t2 = 8*x
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))