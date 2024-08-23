function expect(val) {
	const originalValue = val
	return {
		toBe: function(newVal) {
			if (newVal !== originalValue) {
				throw new Error("Not Equal")
			} else return true },
		notToBe: function(newVal) {
			if (newVal === originalValue) {
				throw new Error("Equal")
			} else return true 
		}
	}
}