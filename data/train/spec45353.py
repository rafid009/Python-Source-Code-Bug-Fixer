import numpy as np 

def function(x):

	i3 = 5
	t2 = x
	x = 5
	paths = []
	try:
		if x < 0:
			t2 = t2/2
			paths.append(1)
		else:
			i3 = x+9
			paths.append(2)
		if i3 < 9:
			i3 = 4+i3
			paths.append(3)
		else:
			i3 = 9*i3
			i3 = i3-2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))