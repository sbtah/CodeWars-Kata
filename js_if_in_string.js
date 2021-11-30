const grzegorz = {
    firstName: 'Grzegorz',
    lastName: 'Zygan',
    age: 2021 - 1983,
    job: 'Ecommerce specialist',
    friends: 'Grzegorz doesnt have any friends!'
}

console.log(`Grzegorz have ${(() => {
    if (typeof grzegorz.friends === 'string') {
        return 0
    } else {
        return grzegorz.friends.length
    }
})()} friends`)