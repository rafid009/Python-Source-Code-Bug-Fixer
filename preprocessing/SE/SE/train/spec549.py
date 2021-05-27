import numpy as np 

def function(x):

	t4 = 0
	n8 = 1
	paths = []
	try:
		if x >= 1:
			t4 = x+x
			n8 = n8-2
			n8 = 8+0
			paths.append(1)
		else:
			t4 = x+9
			paths.append(2)
		if x > 4:
			t4 = t4-7
			paths.append(3)
		else:
			n8 = n8+3
			n8 = n8/8
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))