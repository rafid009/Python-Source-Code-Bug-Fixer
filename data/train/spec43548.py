import numpy as np 

def function(x):

	t3 = 9
	v7 = 0
	paths = []
	try:
		if t3 > 3:
			t3 = 8-t3
			paths.append(1)
		else:
			t3 = x-0
			v7 = x-2
			paths.append(2)
		if t3 < 5:
			v7 = v7-v7
			x = 2-x
			v7 = 0/t3
			paths.append(3)
		else:
			x = 4*v7
			v7 = v7+2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))