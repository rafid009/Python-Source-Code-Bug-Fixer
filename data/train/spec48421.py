import numpy as np 

def function(x):

	t5 = 3
	i3 = x
	x = x
	paths = []
	try:
		if t5 > 4:
			t5 = 9+t5
			t5 = 3+t5
			x = x*1
			paths.append(1)
		else:
			t5 = t5+i3
			paths.append(2)
		if t5 > 8:
			x = x+5
			t5 = 1/t5
			paths.append(3)
		else:
			x = x*2
			t5 = x-x
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		t5 = i3**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))