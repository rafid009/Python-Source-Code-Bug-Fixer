import numpy as np 

def function(x):

	t3 = 1
	e1 = 2
	paths = []
	try:
		if t3 >= 7:
			e1 = t3+1
			x = x+0
			t3 = t3+t3
			paths.append(1)
		else:
			x = x+x
			t3 = 7*5
			paths.append(2)
		if x > 8:
			x = x*5
			x = x/1
			e1 = e1-5
			paths.append(3)
		else:
			x = t3*x
			x = x+e1
			e1 = e1/e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))