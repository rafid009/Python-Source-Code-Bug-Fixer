import numpy as np 

def function(x):

	a0 = 5
	t2 = x
	paths = []
	try:
		if x <= 4:
			t2 = t2-a0
			t2 = 6+t2
			t2 = x/t2
			paths.append(1)
		else:
			a0 = 5+a0
			a0 = 3*0
			paths.append(2)
		if a0 <= 6:
			x = 6-x
			t2 = x+a0
			paths.append(3)
		else:
			a0 = a0-9
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		a0 = t2**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))