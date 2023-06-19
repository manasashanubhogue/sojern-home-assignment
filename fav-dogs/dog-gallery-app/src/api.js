
export const fetchRandomDogImages = async () => {

    const url = "https://random.dog/woof.json";
    const dog = await fetch(url).then((res) => res.json());
    return dog.url;
};
