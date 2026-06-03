import { View, Text, TouchableOpacity } from "react-native";
import { CameraView, useCameraPermissions } from "expo-camera";
import { useRef, useState } from "react";

export default function HomeScreen() {
  const cameraRef = useRef(null);
  const [permission, requestPermission] = useCameraPermissions();
  const [result, setResult] = useState("");

  if (!permission) return <View />;
  
  if (!permission.granted) {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <Text>Camera permission required</Text>
        <TouchableOpacity onPress={requestPermission}>
          <Text style={{ marginTop: 10, color: "blue" }}>
            Grant Permission
          </Text>
        </TouchableOpacity>
      </View>
    );
  }

  const takePicture = async () => {
  try {
    const photo = await cameraRef.current?.takePictureAsync();

    if (!photo) {
      setResult("Failed to capture image");
      return;
    }

    setResult("Authenticating...");

    const formData = new FormData();

    formData.append("image", {
      uri: photo.uri,
      name: "face.jpg",
      type: "image/jpeg",
    } as any);

    const response = await fetch(
      "http://192.168.65.48:5000/auth",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await response.json();

    if (data.status === "success") {
      setResult(`User: ${data.user}`);
    } else {
      setResult(data.msg);
    }
  } catch (error) {
    console.log(error);
    setResult("Connection Error");
  }
};
  return (
    <View style={{ flex: 1 }}>
      <CameraView ref={cameraRef} style={{ flex: 1 }} />

      <TouchableOpacity
        onPress={takePicture}
        style={{
          position: "absolute",
          bottom: 40,
          alignSelf: "center",
          backgroundColor: "white",
          padding: 15,
          borderRadius: 10,
        }}
      >
        <Text>Capture Face</Text>
      </TouchableOpacity>

      <Text style={{ position: "absolute", top: 50, alignSelf: "center" }}>
        {result}
      </Text>
    </View>
  );
}
